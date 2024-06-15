from fastapi import APIRouter,Depends,HTTPException,status
from services.send_email import send_email
from models.schemas.customer import Customer as schemaCustomer, AddCustomer
from sqlalchemy.orm import Session
from db.pg_connection import get_dbpg
from typing import List
from models.models.customer import Customer 
customerRouter =APIRouter()
 #example for sen email

@customerRouter.get("/customers", response_model=List[schemaCustomer])
def allCustomers(db:Session= Depends(get_dbpg)):
    data = db.query(Customer).filter(Customer.status==1)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND ,
            detail="Not customer",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return data

@customerRouter.post("/customer", response_model=schemaCustomer)
def addCustomer( reqCustomer : AddCustomer, db:Session= Depends(get_dbpg)):
    newCustomer = Customer(name=reqCustomer.name, address = reqCustomer.address, number_phone=reqCustomer.number_phone)
    db.add(newCustomer)
    db.commit()
    db.refresh(newCustomer)
    return newCustomer

@customerRouter.get("/customer/{customer_id}",response_model=schemaCustomer)
async def getCustomerId(customer_id:int , db:Session=Depends(get_dbpg)):
    customer = db.query(Customer).filter(Customer.customer_id==customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@customerRouter.put("/customer/{customer_id}",)
def updateCustomer(customer_id:int , req_customer : AddCustomer, db:Session = Depends(get_dbpg)):

    customer = db.query(Customer).filter(Customer.customer_id==customer_id).update({Customer.name : req_customer.name, Customer.address: req_customer.address, Customer.number_phone:req_customer.number_phone})
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.commit()
    return {
        "message":"success"
    }

@customerRouter.delete("/customer/{customer_id}")
def deleteCustomer(customer_id:int , db:Session = Depends(get_dbpg)):
    customer = db.query(Customer).filter(Customer.customer_id==customer_id).update({Customer.status :99})
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.commit()
    return {
        "message":"success delete"
    }
