from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.skill import Skill
from app.models.user_skill import UserSkill
from app.schemas.skill import SkillCreate, SkillOut # Make sure these exist or create simple ones
from app.services.generator import generate_probes_for_skill
from pydantic import BaseModel

router = APIRouter(prefix="/skills", tags=["Skills"])

# Simple Schema for adding a skill
class AddSkillRequest(BaseModel):
    user_id: int
    skill_name: str
    claimed_level: int

@router.post("/add")
def add_new_skill(request: AddSkillRequest, db: Session = Depends(get_db)):
    # 1. Check if Skill exists globally
    skill = db.query(Skill).filter(Skill.name == request.skill_name).first()
    
    if not skill:
        # Create it globally
        skill = Skill(name=request.skill_name)
        db.add(skill)
        db.commit()
        db.refresh(skill)
        
        # ⚡ TRIGGER AI GENERATION ⚡
        success = generate_probes_for_skill(db, skill.name, skill.id)
        
        # SAFETY CHECK: If AI failed, delete the skill to prevent "Zombie State"
        if not success:
            print(f"⚠️ AI Generation failed for {skill.name}. Rolling back...")
            db.delete(skill)
            db.commit()
            raise HTTPException(status_code=500, detail="AI is busy (Rate Limit). Please wait a moment and try again.")
    
    # 2. Link to User (Only if skill exists and has questions)
    user_skill = db.query(UserSkill).filter(
        UserSkill.user_id == request.user_id,
        UserSkill.skill_id == skill.id
    ).first()
    
    if not user_skill:
        user_skill = UserSkill(
            user_id=request.user_id,
            skill_id=skill.id,
            claimed_level=request.claimed_level,
            verified_level=0 
        )
        db.add(user_skill)
        db.commit()
        
    return {"message": f"Skill '{request.skill_name}' added!", "skill_id": skill.id}

@router.get("/")
def get_skills(db: Session = Depends(get_db)):
    return db.query(Skill).all()