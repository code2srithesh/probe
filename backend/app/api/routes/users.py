from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.parser import extract_skills_from_resume
from app.services.generator import generate_probes_for_skill
from app.models.skill import Skill
from app.models.user_skill import UserSkill
from app.models.user import User
from app.models.attempt import Attempt
from pydantic import BaseModel
from typing import List
import shutil
import os

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/{user_id}/upload_resume")
async def scan_resume(user_id: int, file: UploadFile = File(...)):
    # 1. Validate File
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_location = f"temp_{file.filename}"
    
    try:
        # 2. Save
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        
        # 3. Extract (With Error Handling)
        try:
            extracted_skills = extract_skills_from_resume(file_location)
        except Exception as e:
            return {"found_skills": [], "error": str(e)}
            
        return {"found_skills": extracted_skills}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload Error: {str(e)}")
    
    finally:
        # 4. Cleanup
        if os.path.exists(file_location):
            os.remove(file_location)

class ConfirmSkillsRequest(BaseModel):
    skills: List[str]

@router.post("/{user_id}/confirm_skills")
async def confirm_skills(user_id: int, request: ConfirmSkillsRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        user = User(id=user_id, email=f"user{user_id}@example.com", name=f"User {user_id}")
        db.add(user)
        db.commit()

    added_skills = []
    for skill_name in request.skills:
        skill = db.query(Skill).filter(Skill.name == skill_name).first()
        if not skill:
            skill = Skill(name=skill_name)
            db.add(skill)
            db.commit()
            db.refresh(skill)
            generate_probes_for_skill(db, skill.name, skill.id)

        existing_link = db.query(UserSkill).filter(UserSkill.user_id == user_id, UserSkill.skill_id == skill.id).first()
        if not existing_link:
            link = UserSkill(user_id=user_id, skill_id=skill.id, claimed_level=5, verified_level=0)
            db.add(link)
            added_skills.append(skill_name)
    
    db.commit()
    return {"message": "Skills added!", "count": len(added_skills)}

@router.delete("/{user_id}/skills/{skill_id}")
def delete_specific_skill(user_id: int, skill_id: int, db: Session = Depends(get_db)):
    # 1. Check if link exists
    user_skill = db.query(UserSkill).filter(
        UserSkill.user_id == user_id, 
        UserSkill.skill_id == skill_id
    ).first()
    
    if not user_skill:
        raise HTTPException(status_code=404, detail="Skill not found for this user")

    # 2. Delete related Attempts (Clean up history)
    db.query(Attempt).filter(
        Attempt.user_id == user_id,
        Attempt.probe.has(skill_id=skill_id)
    ).delete(synchronize_session=False)

    # 3. Delete the UserSkill link
    db.delete(user_skill)
    db.commit()
    
    return {"message": "Skill removed successfully"}