from sqlalchemy.orm import Session
from app.models import Probe


def select_next_probe(
    db: Session,
    skill_id: int,
    current_depth: int
):
    return (
        db.query(Probe)
        .filter(
            Probe.skill_id == skill_id,
            Probe.depth_level == current_depth + 1
        )
        .first()
    )