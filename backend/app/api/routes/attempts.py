from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.attempt import AttemptCreate, AttemptOut
from app.crud.attempt import create_attempt, get_attempts
from app.api.deps import get_db

router = APIRouter(prefix="/attempts", tags=["Attempts"])


@router.post("/", response_model=AttemptOut)
def create(attempt: AttemptCreate, db: Session = Depends(get_db)):
    return create_attempt(db, attempt)


@router.get("/", response_model=list[AttemptOut])
def read_all(db: Session = Depends(get_db)):
    return get_attempts(db)