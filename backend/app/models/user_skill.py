from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base

class UserSkill(Base):
    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)

    # 1. THE CLAIM: User says "I am an 8/10"
    claimed_level = Column(Integer, default=1) 
    
    # 2. THE REALITY: The highest depth successfully passed
    verified_level = Column(Integer, default=0) 
    
    # 3. THE DECAY: When was this last checked?
    last_verified_at = Column(DateTime(timezone=True), nullable=True)
    
    user = relationship("User", back_populates="user_skills")
    skill = relationship("Skill")