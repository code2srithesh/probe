from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.attempt import Attempt
from app.models.user_skill import UserSkill
from app.schemas.evaluation import EvaluationRequest, EvaluationResponse
from datetime import datetime, timezone
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/evaluate", tags=["Evaluate"])
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@router.post("/{attempt_id}", response_model=EvaluationResponse)
def evaluate_attempt(attempt_id: int, req: EvaluationRequest, db: Session = Depends(get_db)):
    attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")

    # --- START RULE-BASED LOGIC ---
    try:
        # STEP 1: AI ACTS AS "SEMANTIC EXTRACTOR" (The Witness)
        # We don't ask for a grade. We ask for signals.
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Semantic Analyzer. Extract technical signals from the text. Output JSON only."
                },
                {
                    "role": "user",
                    "content": f"""
                    Context Question: "{attempt.probe.question}"
                    Candidate Input: "{req.user_answer}"
                    
                    Analyze the input and return this JSON structure:
                    {{
                        "is_relevant": <bool, true if the answer actually addresses the question>,
                        "contains_core_concept": <bool, true if the fundamental technical concept is present>,
                        "technical_accuracy": <"HIGH", "MEDIUM", "LOW">,
                        "completeness": <"HIGH", "MEDIUM", "LOW">,
                        "feedback": "<1 sentence observation>"
                    }}
                    """
                }
            ]
        )
        
        raw_text = completion.choices[0].message.content
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        signals = json.loads(clean_text)

        # STEP 2: PYTHON ACTS AS "THE JUDGE" (The Rule Engine)
        # This is the "Deterministic" part interviewers love.
        
        passed = False
        score = 0
        feedback = ""

        # Rule 1: Irrelevant answers auto-fail
        if not signals.get("is_relevant", False):
            passed = False
            score = 10
            feedback = "Answer was not relevant to the question."
            
        # Rule 2: Must contain core concept AND have at least Medium accuracy
        elif signals.get("contains_core_concept") and signals.get("technical_accuracy") in ["HIGH", "MEDIUM"]:
            passed = True
            
            # Calculate Score deterministically based on metadata
            base_score = 60
            if signals.get("technical_accuracy") == "HIGH": base_score += 20
            if signals.get("completeness") == "HIGH": base_score += 20
            score = base_score
            feedback = signals.get("feedback", "Good technical understanding.")
            
        else:
            passed = False
            score = 40
            feedback = "Core concept missing or accuracy too low."

    except Exception as e:
        print(f"⚠️ Analysis Failed: {e}")
        # Fallback Rule: Length heuristic
        score = 80 if len(req.user_answer) > 20 else 30
        passed = score >= 60
        feedback = "System Backup: Manual review required."
    # --- END RULE-BASED LOGIC ---

    # --- DATABASE UPDATES & RETURN (This was missing!) ---
    attempt.score = score
    attempt.passed = passed
    attempt.feedback = feedback
    attempt.completed_at = datetime.now(timezone.utc)
    
    current_level = 0
    
    # Check if we need to verify a level
    user_skill = db.query(UserSkill).filter(
        UserSkill.user_id == attempt.user_id,
        UserSkill.skill_id == attempt.probe.skill_id
    ).first()
    
    if user_skill:
        current_level = user_skill.verified_level
        if passed:
            # Logic: If they passed a Level 3 probe, they are verified at Level 3.
            # But we only increase, never decrease (High-Water Mark).
            new_level = max(user_skill.verified_level, attempt.probe.depth_level)
            user_skill.verified_level = new_level
            user_skill.last_verified_at = datetime.now(timezone.utc)
            current_level = new_level

    db.commit()

    return {
        "passed": passed, 
        "score": score, 
        "feedback": feedback,
        "new_verified_level": current_level
    }