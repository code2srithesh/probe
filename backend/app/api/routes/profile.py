from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import User, UserSkill, Skill
from app.domain.decay import is_skill_stale

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("/{user_id}")
def public_profile(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    records = (
        db.query(UserSkill, Skill)
        .join(Skill, Skill.id == UserSkill.skill_id)
        .filter(UserSkill.user_id == user_id)
        .all()
    )

    skills = []

    for user_skill, skill in records:
        skills.append({
            "skill": skill.name,
            "verified_depth": user_skill.verified_depth,
            "last_verified": user_skill.last_verified,
            "stale": is_skill_stale(user_skill.last_verified)
        })

    return {
        "name": user.name,
        "email": user.email,
        "verified_skills": skills
    }