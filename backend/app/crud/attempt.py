from sqlalchemy.orm import Session
from app.models.attempt import Attempt
from app.schemas.attempt import AttemptCreate

def create_attempt(db: Session, attempt: AttemptCreate):
    db_attempt = Attempt(
        user_id=attempt.user_id,
        probe_id=attempt.probe_id,
        # FIX: Don't look for score in the input. Set it to 0 initially.
        score=0,
        passed=False
    )
    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)
    return db_attempt

def get_attempts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Attempt).offset(skip).limit(limit).all()