from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Probe(Base):
    __tablename__ = "probes"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)

    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)

    skill = relationship("Skill", back_populates="probes")
    attempts = relationship("Attempt", back_populates="probe")