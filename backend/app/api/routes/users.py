from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_users
from app.api.deps import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserOut)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=list[UserOut])
def read_all(db: Session = Depends(get_db)):
    return get_users(db)