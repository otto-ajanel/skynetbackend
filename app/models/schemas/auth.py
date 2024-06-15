from pydantic import BaseModel
class Token(BaseModel):
    access_token: str
    token_type: str
    rol_id:int
    user_id:int
    name:str