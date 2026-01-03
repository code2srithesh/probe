from sqlalchemy.orm import Session
from app.models import Attempt, Probe


def is_depth_failed(
    db: Session,
    user_id: int,
    skill_id: int,
    depth: int,
    threshold: int = 2
) -> bool:
    """
    Returns True if user failed `threshold` times at this depth.
    """

    failures = (
        db.query(Attempt)
        .join(Probe, Attempt.probe_id == Probe.id)
        .filter(
            Attempt.user_id == user_id,
            Probe.skill_id == skill_id,
            Probe.depth_level == depth,
            Attempt.passed == False
        )
        .count()
    )

    return failures >= threshold