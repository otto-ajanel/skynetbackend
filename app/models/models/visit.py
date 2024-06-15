from sqlalchemy import Column, Integer, String, JSON
from db.pg_connection import Base
class Visit(Base):

    __tablename__="visits"
    visit_id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    subject=Column(String)
    description=Column(String)
    address=Column(String)
    latitud=Column(String)
    longitud=Column(String)
    fecha=Column(String)
    status=Column(Integer, default=1)