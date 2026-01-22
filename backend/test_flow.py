import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from app.database import SessionLocal
from app.crud.attempt import create_attempt
from app.schemas.attempt import AttemptCreate
from app.schemas.evaluation import EvaluationRequest
from app.api.routes.evaluate import evaluate_attempt
from app.models.user_skill import UserSkill

def test_full_flow():
    db = SessionLocal()
    print("🚀 Starting User Flow Test...")

    # 1. SETUP: IDs from our Seed Data
    user_id = 1  # Srithesh
    probe_id = 1 # The 'Level 1' Java Question

    # 2. ACTION: User starts the quiz (Create Attempt)
    print("\n1️⃣  User starts the quiz...")
    attempt_in = AttemptCreate(user_id=user_id, probe_id=probe_id)
    attempt = create_attempt(db, attempt_in)
    print(f"   -> Attempt Created! ID: {attempt.id}")

   # 3. ACTION: User answers the question (Evaluate)
    print("\n2️⃣  User submits answer...")
    
    # A complete answer that satisfies the "Senior Interviewer"
    user_answer = """
    The JDK (Java Development Kit) is the full toolkit for developers, including the compiler (javac).
    The JRE (Java Runtime Environment) is for running applications and includes libraries.
    The JVM (Java Virtual Machine) is the engine that actually executes the bytecode on the hardware.
    """
    
    eval_req = EvaluationRequest(user_answer=user_answer)
    
    # We call the evaluation function directly to test logic
    result = evaluate_attempt(attempt.id, eval_req, db)
    
    print(f"   -> Passed: {result.passed}")
    print(f"   -> Score: {result.score}")
    print(f"   -> New Verified Level: {result.new_verified_level}")

    # 4. VERIFICATION: Check the Database directly
    print("\n3️⃣  Verifying Database State...")
    user_skill = db.query(UserSkill).filter(
        UserSkill.user_id == user_id, 
        UserSkill.skill_id == 1
    ).first()
    
    if user_skill.verified_level == 1:
        print("✅ SUCCESS: User's Verified Level updated to 1!")
        print(f"   Last Verified At: {user_skill.last_verified_at}")
    else:
        print(f"❌ FAILURE: User Level is {user_skill.verified_level}, expected 1.")

    db.close()

if __name__ == "__main__":
    test_full_flow()