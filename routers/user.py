from fastapi import APIRouter, Depends, status
from schemas import User, ShowUser
import models as models 
from sqlalchemy.orm import Session
from database import get_db
from repository.user import get_user_id, post_user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/{id}", response_model=ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return get_user_id(id, db)

@router.post("", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    return post_user(request, db)