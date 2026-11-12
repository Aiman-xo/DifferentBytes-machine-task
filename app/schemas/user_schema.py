from pydantic import BaseModel

class UserCreation(BaseModel):
    username:str
    password:int
    email:str
