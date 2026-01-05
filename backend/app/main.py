from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import base
from app.api.routes import users, skills, attempts, evaluate, profile
from fastapi.staticfiles import StaticFiles


# Create Tables
base.Base.metadata.create_all(bind=engine)

app = FastAPI(title="PROBE | Skill Reality Engine")

# ---------------------------------------------------------
# 🔓 CORS SETTINGS (THE KEY TO FIXING UPLOAD)
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",  # VS Code Live Server
        "http://localhost:5500",  # Alternative URL
        "*"                       # Allow everything (Safety net)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------------------------------

# Register Routes
app.include_router(users.router)
app.include_router(skills.router)
app.include_router(attempts.router)
app.include_router(evaluate.router)
app.include_router(profile.router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")


@app.get("/")
def read_root():
    return {"status": "System Online", "engine": "Groq Llama 3"}