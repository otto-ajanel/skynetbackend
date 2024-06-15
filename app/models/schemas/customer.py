from typing import Optional
from pydantic import BaseModel
class Customer(BaseModel):
    customer_id: int
    name:str
    address:str
    status:int
    number_phone:Optional[str]

    class Config:
        orm_mode=True

class AddCustomer(BaseModel):
    name:str
    address:str
    number_phone:str

    class Config:
        orm_mode:True