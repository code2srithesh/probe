from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.core.evaluator import evaluate_answer
from app.domain.decay import is_skill_stale

from app.models import Probe, Attempt, UserSkill
from app.schemas.attempt import AttemptCreate
from app.domain.selector import select_next_probe
from app.domain.failure import is_depth_failed

router = APIRouter(prefix="/evaluate", tags=["Evaluate"])


@router.post("/")
def evaluate(attempt: AttemptCreate, db: Session = Depends(get_db)):
    probe = db.query(Probe).filter(Probe.id == attempt.probe_id).first()

    passed = evaluate_answer(
        answer=attempt.answer,
        depth=probe.depth_level
    )

    now = datetime.utcnow()

    # save attempt
    db_attempt = Attempt(
        user_id=attempt.user_id,
        probe_id=probe.id,
        passed=passed,
        evaluated_depth=probe.depth_level,
        created_at=now
    )
    db.add(db_attempt)
    db.commit()

    # get user skill
    user_skill = (
        db.query(UserSkill)
        .filter(
            UserSkill.user_id == attempt.user_id,
            UserSkill.skill_id == probe.skill_id
        )
        .first()
    )

    # check failure confirmation FIRST
    failure_confirmed = False
    if not passed:
        failure_confirmed = is_depth_failed(
            db=db,
            user_id=attempt.user_id,
            skill_id=probe.skill_id,
            depth=probe.depth_level
        )

    # update on pass
    if passed:
        if not user_skill:
            user_skill = UserSkill(
                user_id=attempt.user_id,
                skill_id=probe.skill_id,
                verified_depth=probe.depth_level,
                last_verified=now
            )
            db.add(user_skill)
        else:
            if probe.depth_level > user_skill.verified_depth:
                user_skill.verified_depth = probe.depth_level
            user_skill.last_verified = now

        db.commit()

    # 🔒 freeze boundary on confirmed failure
    if not passed and failure_confirmed:
        if user_skill and probe.depth_level <= user_skill.verified_depth:
            user_skill.verified_depth = probe.depth_level - 1
            db.commit()

    # select next probe ONLY if passed
    next_probe = None
    if passed:
        next_probe_obj = select_next_probe(
            db,
            skill_id=probe.skill_id,
            current_depth=probe.depth_level
        )

        if next_probe_obj:
            next_probe = {
                "probe_id": next_probe_obj.id,
                "question": next_probe_obj.question,
                "depth": next_probe_obj.depth_level
            }

    return {
        "passed": passed,
        "depth": probe.depth_level,
        "failure_confirmed": failure_confirmed,
        "next_probe": next_probe
    }

@router.get("/next-probe")
def get_next_probe(
    user_id: int,
    skill_id: int,
    db: Session = Depends(get_db)
):
    user_skill = (
        db.query(UserSkill)
        .filter(
            UserSkill.user_id == user_id,
            UserSkill.skill_id == skill_id
        )
        .first()
    )

    current_depth = user_skill.verified_depth if user_skill else 0

    next_probe = select_next_probe(
        db=db,
        skill_id=skill_id,
        current_depth=current_depth
    )

    if not next_probe:
        return {"message": "No more probes available"}

    return {
        "probe_id": next_probe.id,
        "question": next_probe.question,
        "depth": next_probe.depth_level,
        "probe_type": next_probe.probe_type
    }