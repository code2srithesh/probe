from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.skill import SkillCreate, SkillOut
from app.crud.skill import create_skill, get_skills
from app.api.deps import get_db

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.post("/", response_model=SkillOut)
def create(skill: SkillCreate, db: Session = Depends(get_db)):
    return create_skill(db, skill)


@router.get("/", response_model=list[SkillOut])
def read_all(db: Session = Depends(get_db)):
    return get_skills(db)