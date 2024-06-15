from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas.user import User
from models.models.user_model import User as UserModel
from models.schemas.auth import Token
from sqlalchemy.orm import Session
from db.pg_connection import get_dbpg
from typing import List

import jwt
auth= APIRouter()
@auth.get("/test" ,tags=["start"])
def read():

    return {"hello":"I'm fastapi"}

@auth.post("/login", response_model=Token)
def login(user_sign:User  , db:Session = Depends(get_dbpg)):

    result = db.query(UserModel).filter(UserModel.email==user_sign.email, UserModel.password==user_sign.password).first()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND ,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    tokenGenerate=jwt.encode({"email":result.email,"rol_id":result.rol_id,"user_id":result.user_id},"Ajanel", algorithm="HS256")

    return {
        "access_token":tokenGenerate,
        "token_type":"BearToken",
        "rol_id":result.rol_id,
        "user_id":result.user_id,
        "name":result.name
    }

