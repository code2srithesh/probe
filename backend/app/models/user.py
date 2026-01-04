from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)

    # Links to the User's history of attempts
    attempts = relationship("Attempt", back_populates="user")
    
    # NEW: Links to the User's skill levels (Claims vs Reality)
    user_skills = relationship("UserSkill", back_populates="user")