from fastapi import FastAPI

from app.core.database import engine
from app.models.base import Base

from app.api.routes import (
    users_router,
    skills_router,
    probes_router,
    attempts_router
)

app = FastAPI(title="Probe API")

# create tables
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(users_router)
app.include_router(skills_router)
app.include_router(probes_router)
app.include_router(attempts_router)


@app.get("/")
def root():
    return {"status": "Probe backend running"}