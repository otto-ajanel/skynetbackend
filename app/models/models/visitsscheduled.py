from sqlalchemy import Column,Integer,String, DateTime, func
from db.pg_connection import Base
from datetime import datetime
class Schedule(Base):
    __tablename__= "visitsscheduled"
    visitsscheduled_id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    userasigned_id=Column(Integer)
    usercreate_id=Column(Integer)
    datecreate=Column(DateTime, default=func.now())
    visit_id= Column(Integer)

