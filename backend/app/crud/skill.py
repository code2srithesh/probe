from sqlalchemy.orm import Session
from app.models.skill import Skill
from app.schemas.skill import SkillCreate


def create_skill(db: Session, skill: SkillCreate):
    db_skill = Skill(name=skill.name)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skills(db: Session):
    return db.query(Skill).all()