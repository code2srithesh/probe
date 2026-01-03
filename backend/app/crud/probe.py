from sqlalchemy.orm import Session
from app.models.probe import Probe
from app.schemas.probe import ProbeCreate


def create_probe(db: Session, probe: ProbeCreate):
    db_probe = Probe(
        question=probe.question,
        skill_id=probe.skill_id
    )
    db.add(db_probe)
    db.commit()
    db.refresh(db_probe)
    return db_probe


def get_probes(db: Session):
    return db.query(Probe).all()