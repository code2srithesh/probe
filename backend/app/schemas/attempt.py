from pydantic import BaseModel


class AttemptBase(BaseModel):
    user_id: int
    probe_id: int
    score: int


class AttemptCreate(AttemptBase):
    pass


class AttemptOut(AttemptBase):
    id: int

    class Config:
        orm_mode = True