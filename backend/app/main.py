from fastapi import FastAPI
from app.api.routes.evaluate import router as evaluate_router
from app.api.routes.skills_snapshot import router as skills_snapshot_router
from app.core.database import engine
from app.models.base import Base
from app.api.routes.profile import router as profile_router



from app.api.routes import (
    users_router,
    skills_router,
    probes_router,
    attempts_router
)

app = FastAPI(title="Probe API")
app.include_router(skills_snapshot_router)
app.include_router(profile_router)

# create tables
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(users_router)
app.include_router(skills_router)
app.include_router(probes_router)
app.include_router(attempts_router)
app.include_router(evaluate_router)


@app.get("/")
def root():
    return {"status": "Probe backend running"}