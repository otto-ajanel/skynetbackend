from pydantic import BaseModel
class VisitCreate(BaseModel):
    subject:str   
    description:str
    address:str
    latitud:str 
    longitud:str 
    usercreate:int
    customer_id:int
    userasigned:int
    fecha:str
    class config:
        orm_mode:True

class Visits(BaseModel):
    subject:str   
    description:str
    address:str
    latitud:str 
    longitud:str 
    usercreate:int
    customer_id:int
    userasigned:int
    fecha:str
    class config:
        orm_mode:True