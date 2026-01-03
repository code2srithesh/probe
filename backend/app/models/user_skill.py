from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.models.base import Base
from datetime import datetime

class UserSkill(Base):
    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)

    verified_depth = Column(Integer, nullable=False)
    last_verified = Column(DateTime, default=datetime.utcnow)