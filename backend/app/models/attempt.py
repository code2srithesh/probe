from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    probe_id = Column(Integer, ForeignKey("probes.id"), nullable=False)
    score = Column(Integer, nullable=False)

    user = relationship("User", back_populates="attempts")
    probe = relationship("Probe", back_populates="attempts")