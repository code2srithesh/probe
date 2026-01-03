from sqlalchemy.orm import Session
from app.models.attempt import Attempt
from app.schemas.attempt import AttemptCreate


def create_attempt(db: Session, attempt: AttemptCreate):
    db_attempt = Attempt(
        user_id=attempt.user_id,
        probe_id=attempt.probe_id,
        score=attempt.score
    )
    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)
    return db_attempt


def get_attempts(db: Session):
    return db.query(Attempt).all()