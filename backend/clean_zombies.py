from app.database import SessionLocal
from app.models.skill import Skill
from app.models.probe import Probe
from app.models.user_skill import UserSkill

db = SessionLocal()

# Find skills with 0 probes
zombies = []
all_skills = db.query(Skill).all()

for skill in all_skills:
    probe_count = db.query(Probe).filter(Probe.skill_id == skill.id).count()
    if probe_count == 0:
        zombies.append(skill)

print(f"🧟 Found {len(zombies)} Zombie Skills (No questions generated).")

for z in zombies:
    print(f"   - Deleting {z.name}...")
    # Delete links first
    db.query(UserSkill).filter(UserSkill.skill_id == z.id).delete()
    # Delete skill
    db.delete(z)

db.commit()
print("✅ Database Cleaned. No more infinite loading.")