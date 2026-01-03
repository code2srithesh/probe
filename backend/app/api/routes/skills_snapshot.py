
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.models import UserSkill, Skill
from app.domain.decay import is_skill_stale

router = APIRouter(prefix="/skills", tags=["Skill Snapshot"])


@router.get("/snapshot/{user_id}")
def skill_snapshot(user_id: int, db: Session = Depends(get_db)):
    records = (
        db.query(UserSkill, Skill)
        .join(Skill, Skill.id == UserSkill.skill_id)
        .filter(UserSkill.user_id == user_id)
        .all()
    )

    snapshot = []

    for user_skill, skill in records:
        stale = is_skill_stale(user_skill.last_verified)

        snapshot.append({
            "skill": skill.name,
            "verified_depth": user_skill.verified_depth,
            "last_verified": user_skill.last_verified,
            "stale": stale
        })

    return {
        "user_id": user_id,
        "skills": snapshot
    }