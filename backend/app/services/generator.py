import os
from groq import Groq
from app.models.probe import Probe
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_probes_for_skill(db: Session, skill_name: str, skill_id: int):
    print(f"⚡ Groq Generating probes for: {skill_name}...")
    
    try:
        # UPDATED MODEL NAME
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Senior Interviewer. Return ONLY raw text formatted exactly as requested."
                },
                {
                    "role": "user",
                    "content": f"""
                    Generate 3 distinct interview questions for: "{skill_name}".
                    
                    Format EXACTLY like this (3 lines, no markdown):
                    1|explain|Question text here
                    2|debug|Question text here
                    3|design|Question text here
                    """
                }
            ],
            temperature=0.7,
        )

        response_text = completion.choices[0].message.content
        lines = response_text.strip().split('\n')
        
        valid_probes = []
        for line in lines:
            parts = line.split('|')
            if len(parts) >= 3:
                valid_probes.append(parts)

        if not valid_probes: raise Exception("Groq returned bad format")

        for parts in valid_probes:
            probe = Probe(
                skill_id=skill_id,
                depth_level=int(parts[0].strip()),
                probe_type=parts[1].strip(),
                question=parts[2].strip()
            )
            db.add(probe)
        
        db.commit()
        print(f"✅ Groq Success: Generated {len(valid_probes)} probes.")
        return True

    except Exception as e:
        print(f"⚠️ Groq Failed ({e}). Using MOCK MODE.")
        mock_questions = [
            f"1|explain|Explain the core concepts of {skill_name}.",
            f"2|debug|Describe a common bug in {skill_name} and how to fix it.",
            f"3|design|How is {skill_name} used in production?"
        ]
        for line in mock_questions:
            parts = line.split('|')
            db.add(Probe(
                skill_id=skill_id,
                depth_level=int(parts[0].strip()),
                probe_type=parts[1].strip(),
                question=parts[2].strip()
            ))
        db.commit()
        return True