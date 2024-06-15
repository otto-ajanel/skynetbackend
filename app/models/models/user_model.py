from sqlalchemy import Column, Integer, String, JSON
from db.pg_connection import Base
class User(Base):
    __tablename__ ="user"

    user_id=Column(Integer, primary_key=True, index=True,autoincrement=True )
    email=Column(String, index=True)
    password=Column(String)
    name =Column(String)
    lastname=Column(String)
    permissions=Column(JSON, nullable=False)
    rol_id=Column(Integer)
    status= Column(Integer ,default=1)

