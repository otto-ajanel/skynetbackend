from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def valide_token(token: str = Depends(oauth2_scheme)):
    try:
        
        payload = jwt.decode(token, "Ajanel", algorithms="HS256")
        return payload
    
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
