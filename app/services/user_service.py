from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreation
from app.models.user_model import User
from fastapi import HTTPException

def add_user_service(user:UserCreation,db:Session):
    try:
        user = db.query(User).filter(User.username == user.username).first()
        if not user:
            raise HTTPException(status_code=400,detail='user already exists')

        new_user = User(
            username = user.username,
            email = user.email,
            password = user.password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return user
    except Exception as e :
        raise HTTPException(status_code=400,detail=str(e))

    