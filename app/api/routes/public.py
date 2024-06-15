from fastapi import APIRouter

public= APIRouter()

@public.get("/" ,tags=["start"])
def read_root():
    return {"hello":"I'm Otto Ajanel from Gautemala City"}