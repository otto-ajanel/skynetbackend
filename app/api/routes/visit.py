from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from models.schemas.visit import VisitCreate 
from models.models.visit import Visit
from models.models.visitsscheduled import Schedule
from db.pg_connection import get_dbpg
from services.send_email import send_email
from models.models.customer import Customer

visitRouter=APIRouter()

@visitRouter.post("/visit")
def addVisit(req:VisitCreate, db:Session = Depends(get_dbpg)):
    newVisit= Visit(subject =req.subject, description=req.description, address=req.address, latitud=req.latitud, longitud=req.longitud, fecha= req.fecha )
    db.add(newVisit)
    db.commit()
    db.refresh(newVisit)
    
    newschedule= Schedule(usercreate_id=req.usercreate, userasigned_id=req.userasigned, visit_id=newVisit.visit_id)
    db.add(newschedule)
    db.commit()
    db.refresh(newschedule)
    return {
        "message":"succcess create"
    }

@visitRouter.get("/visits")
def allVisits(user_id:int, rol_id:int, db:Session =Depends(get_dbpg)):

    results=[]
    if(rol_id==1):
        query = text("select v.* from visits v inner join visitsscheduled vs on v.visit_id =vs.visit_id where v.status =1 order by v.visit_id desc")

        result =db.execute(query)
        results = result.fetchall()
    if(rol_id==2):
        query = text("select v.* from visits v inner join visitsscheduled vs on v.visit_id =vs.visit_id where v.status =1 and vs.usercreate_id=:user_id order by v.visit_id desc")

        result =db.execute(query,{"user_id":user_id})
        results = result.fetchall()
    if(rol_id==3):
        query = text("select v.* from visits v inner join visitsscheduled vs on v.visit_id =vs.visit_id where v.status =1 and vs.userasigned_id=:user_id order by v.visit_id desc")

        result =db.execute(query,{"user_id":user_id})
        results = result.fetchall()

    if not results:
        raise HTTPException(status_code=404, detail="User not found or no visits found")

    column_names = result.keys()
    
    
    users_with_visits = [
        dict(zip(column_names, row))
        for row in results
    ]

    return users_with_visits


@visitRouter.get("/visitfinish")
def finishVisit(customer_id:int, visit_id:int, db:Session =Depends(get_dbpg)):
    customer =db.query(Customer).filter(Customer.customer_id==customer_id).first()
    visit =db.query(Visit).filter(Visit.visit_id==visit_id).update({Visit.status:9})
    db.commit()
    cuerpo = "Se notifica que la visita #" + str(visit_id) +" ha sido concluido"
    send_email("Visita de Skynet",cuerpo, customer.address)

    return {
        "message"
    }