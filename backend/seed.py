import sys
import os
from sqlalchemy.orm import Session
from datetime import datetime, timezone, timedelta

# Add current directory to path
sys.path.append(os.getcwd())

from app.database import SessionLocal, engine
from app.models.base import Base
from app.models.user import User
from app.models.skill import Skill
from app.models.probe import Probe
from app.models.user_skill import UserSkill

def seed_data():
    db = SessionLocal()
    
    # Optional: Wipe everything clean first to avoid duplicates
    print("🧹 Cleaning old data...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    print("🌱 Seeding rich data...")

    # 1. Create a User
    user = User(email="srithesh@example.com", name="Srithesh")
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"✅ Created User: {user.name}")

    # 2. Define Skills & Questions
    skills_data = [
        {
            "name": "Java",
            "probes": [
                (1, "explain", "What is the difference between JDK, JRE, and JVM?"),
                (2, "debug", "Explain the contract between hashCode() and equals(). What happens if you break it?"),
                (3, "design", "How does Garbage Collection impact latency in high-frequency trading systems?")
            ],
            "claimed": 8,
            "verified": 1, # User has passed level 1
            "verified_at": datetime.now(timezone.utc)
        },
        {
            "name": "Python",
            "probes": [
                (1, "explain", "What are Python decorators and how do they work?"),
                (2, "code", "Explain the difference between deepcopy and shallow copy in Python."),
                (3, "design", "How does the Global Interpreter Lock (GIL) affect multi-threaded Python programs?")
            ],
            "claimed": 9,
            "verified": 0, # Not verified yet
            "verified_at": None
        },
        {
            "name": "System Design",
            "probes": [
                (1, "explain", "What is the difference between vertical scaling and horizontal scaling?"),
                (2, "design", "Design a URL shortener like Bit.ly. usage of database vs cache?"),
                (3, "design", "How would you design a rate limiter for a distributed API?")
            ],
            "claimed": 6,
            "verified": 2, # User is decent at this
            "verified_at": datetime.now(timezone.utc) - timedelta(days=40) # OLD! This should show as "Decaying"
        }
    ]

    for data in skills_data:
        # Create Skill
        skill = Skill(name=data["name"])
        db.add(skill)
        db.commit()
        db.refresh(skill)
        
        # Create Probes
        for level, p_type, question in data["probes"]:
            probe = Probe(
                skill_id=skill.id,
                depth_level=level,
                probe_type=p_type,
                question=question
            )
            db.add(probe)
        
        # Link to User
        user_skill = UserSkill(
            user_id=user.id, 
            skill_id=skill.id, 
            claimed_level=data["claimed"], 
            verified_level=data["verified"],
            last_verified_at=data["verified_at"]
        )
        db.add(user_skill)
        print(f"✅ Added Skill: {skill.name}")

    db.commit()
    db.close()
    print("🎉 Mega Seeding complete!")

if __name__ == "__main__":
    seed_data()