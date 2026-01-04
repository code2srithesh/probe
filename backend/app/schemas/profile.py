from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SkillProfile(BaseModel):
    skill_name: str
    skill_id: int             # <--- Added this to be safe
    claimed_level: int
    verified_level: int
    last_verified_at: Optional[datetime] = None
    status: str
    next_probe_id: Optional[int] = None  # <--- NEW: The exact ID of the next test

class UserProfile(BaseModel):
    name: str
    email: str
    skills: List[SkillProfile]