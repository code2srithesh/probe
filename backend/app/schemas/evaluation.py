from pydantic import BaseModel

class EvaluationRequest(BaseModel):
    user_answer: str

class EvaluationResponse(BaseModel):
    passed: bool
    score: int
    feedback: str
    new_verified_level: int