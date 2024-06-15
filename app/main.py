from fastapi import FastAPI, dependencies, Depends
from fastapi.middleware.cors import CORSMiddleware
from api.routes.public import public
from api.routes.auth import auth
from api.routes.customer import customerRouter
from api.routes.user import userRouter
from services.authUtils import valide_token
from db.pg_connection import engine
from api.routes.visit import visitRouter


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(public)
app.include_router(auth)

app.include_router(customerRouter,dependencies=[Depends(valide_token)])
app.include_router(userRouter, dependencies=[Depends(valide_token)])
app.include_router(visitRouter, dependencies=[Depends(valide_token)])

