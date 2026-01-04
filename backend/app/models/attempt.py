from sqlalchemy import Boolean, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    probe_id = Column(Integer, ForeignKey("probes.id"), nullable=False)
    
    score = Column(Integer, nullable=False)
    passed = Column(Boolean, default=False)
    evaluated_depth = Column(Integer)
    
    # NEW: Timestamps allow us to calculate "Skill Decay"
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="attempts")
    probe = relationship("Probe", back_populates="attempts")