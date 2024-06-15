from fastapi import APIRouter,Depends,HTTPException,status
from models.schemas.user import UserCreate, Users
from sqlalchemy.orm import Session
from db.pg_connection import get_dbpg
from typing import List
from models.models.user_model import User 
userRouter =APIRouter()
 

@userRouter.get("/users", response_model=List[Users])
def allUsers(db:Session= Depends(get_dbpg)):
    data = db.query(User).filter(User.status==1)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND ,
            detail="Not user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return data

@userRouter.post("/user", response_model=UserCreate)
def addUser( reqUser : UserCreate, db:Session= Depends(get_dbpg)):
    newUser = User(name=reqUser.name, email = reqUser.email, password =reqUser.password, lastname= reqUser.lastname, rol_id= reqUser.rol_id)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser



@userRouter.put("/user/{user_id}",)
def updateUser(user_id:int , rol_id:int, db:Session = Depends(get_dbpg)):

    customer = db.query(User).filter(User.user_id==user_id).update({User.rol_id : rol_id})
    if not customer:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    return {
        "message":"success"
    }

@userRouter.delete("/user/{user_id}")
def deleteCustomer(user_id:int , db:Session = Depends(get_dbpg)):
    user = db.query(User).filter(User.user_id==user_id).update({User.status :99})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    return {
        "message":"success delete"
    }
