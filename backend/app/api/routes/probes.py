from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.probe import ProbeCreate, ProbeOut
from app.crud.probe import create_probe, get_probes
from app.api.deps import get_db

router = APIRouter(prefix="/probes", tags=["Probes"])


@router.post("/", response_model=ProbeOut)
def create(probe: ProbeCreate, db: Session = Depends(get_db)):
    return create_probe(db, probe)


@router.get("/", response_model=list[ProbeOut])
def read_all(db: Session = Depends(get_db)):
    return get_probes(db)