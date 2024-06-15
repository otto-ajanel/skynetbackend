from sqlalchemy import Column, Integer, String
from db.pg_connection import Base
class Customer(Base):
    __tablename__="customer"

    customer_id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String)
    address=Column(String)
    status=Column(Integer, default=1)
    number_phone=Column(String)