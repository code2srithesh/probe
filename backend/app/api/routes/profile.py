from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.database import get_db
from app.models.user import User
from app.models.probe import Probe  # <--- Make sure to import Probe
from app.schemas.profile import UserProfile, SkillProfile

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/{user_id}", response_model=UserProfile)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    # 1. Try to find the user
    user = db.query(User).filter(User.id == user_id).first()
    
    # 2. If user doesn't exist, AUTO-CREATE them (Lazy Registration)
    if not user:
        print(f"👤 User {user_id} not found. Creating new user...")
        user = User(
            id=user_id, 
            email=f"user{user_id}@example.com", 
            name=f"User {user_id}"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # 3. Now fetch their skills (which will be empty for a new user)
    skill_list = []
    for us in user.user_skills:
        # Determine Status
        status = "Unverified"
        if us.verified_level > 0:
            status = "Verified"
            if us.last_verified_at:
                days_since = (datetime.now(timezone.utc) - us.last_verified_at).days
                if days_since > 30:
                    status = "Decaying"

        # Find Next Probe
        target_level = us.verified_level + 1
        
        if target_level > 3: 
            next_probe_id = None 
        else:
            next_probe = db.query(Probe).filter(
                Probe.skill_id == us.skill_id,
                Probe.depth_level == target_level
            ).first()
            
            # If no probe exists, send -1 to signal "Generating..."
            next_probe_id = next_probe.id if next_probe else -1 

        skill_list.append(SkillProfile(
            skill_name=us.skill.name,
            skill_id=us.skill.id,
            claimed_level=us.claimed_level,
            verified_level=us.verified_level,
            last_verified_at=us.last_verified_at,
            status=status,
            next_probe_id=next_probe_id 
        ))

    return UserProfile(
        name=user.name,
        email=user.email,
        skills=skill_list
    )