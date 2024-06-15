from  pydantic import BaseModel
class UserBase(BaseModel):
    email:str
    password:str

class UserCreate(UserBase):
    name: str
    lastname:str
    rol_id:int
class User(UserBase):
    
    class Config:
        orm_mode=True

class Users(UserBase):
    user_id:int
    name: str
    lastname:str
    rol_id:int