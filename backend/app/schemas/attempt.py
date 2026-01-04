from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# New: A mini-schema just for the question info
class ProbeInfo(BaseModel):
    question: str
    depth_level: int
    
    class Config:
        from_attributes = True

class AttemptCreate(BaseModel):
    user_id: int
    probe_id: int

class AttemptOut(BaseModel):
    id: int
    user_id: int
    probe_id: int
    score: Optional[int] = None
    passed: bool
    created_at: datetime
    
    # NEW: The attempt now carries the probe details with it
    probe: ProbeInfo 

    class Config:
        from_attributes = True