from fastapi import APIRouter,Depends
from app.core.database import get_db
from app.schemas.user_schema import UserCreation
from sqlalchemy.orm import Session
from app.services.user_service import add_user_service

router = APIRouter(prefix='/user')

@router.post('/add')
def add_user(user:UserCreation,db:Session = Depends(get_db)):
    return add_user_service(user,db)