import sys
import os
from sqlalchemy import text

# Add current directory to path so we can find 'app'
sys.path.append(os.getcwd())

from app.database import engine
from app.models.base import Base

# Import all models
from app.models.user import User
from app.models.skill import Skill
from app.models.probe import Probe
from app.models.attempt import Attempt
from app.models.user_skill import UserSkill

print("☢️  Initiating NUCLEAR database reset...")

with engine.connect() as connection:
    # We turn off the transaction momentarily to execute raw drops
    connection.execute(text("COMMIT"))
    
    # 1. Force drop the "Zombie" table causing the error
    print("🧟 Dropping zombie table 'probe_attempts'...")
    connection.execute(text("DROP TABLE IF EXISTS probe_attempts CASCADE"))
    
    # 2. Force drop all known tables with CASCADE (destroys links)
    print("🗑️  Dropping known tables...")
    connection.execute(text("DROP TABLE IF EXISTS attempts CASCADE"))
    connection.execute(text("DROP TABLE IF EXISTS user_skills CASCADE"))
    connection.execute(text("DROP TABLE IF EXISTS probes CASCADE"))
    connection.execute(text("DROP TABLE IF EXISTS skills CASCADE"))
    connection.execute(text("DROP TABLE IF EXISTS users CASCADE"))
    
    # 3. Drop alembic_version if it exists (cleanup)
    connection.execute(text("DROP TABLE IF EXISTS alembic_version CASCADE"))

    print("✅ All tables dropped.")

# 4. Recreate everything from scratch
print("🏗️  Recreating tables from fresh models...")
Base.metadata.create_all(bind=engine)

print("🚀 Database reset complete! System is clean.")