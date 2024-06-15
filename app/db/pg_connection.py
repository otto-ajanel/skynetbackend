from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL ="postgresql://postgres:49720012@localhost:5432/erppgdb"

engine=create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit =False, autoflush=False, bind=engine)
Base = declarative_base()

def get_dbpg():

    db=SessionLocal()

    try:

        yield db
    finally:
        db.close()