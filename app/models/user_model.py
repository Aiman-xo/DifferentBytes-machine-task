from app.core.database import Base
from sqlalchemy import Column,String,Integer

class User(Base):
    __tablename__ = 'user1'
    id = Column(Integer,primary_key=True,nullable=False)
    username = Column(String(100),nullable=False,unique=True)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)