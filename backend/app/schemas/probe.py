from pydantic import BaseModel


class ProbeBase(BaseModel):
    question: str
    skill_id: int


class ProbeCreate(ProbeBase):
    pass


class ProbeOut(ProbeBase):
    id: int

    class Config:
        orm_mode = True