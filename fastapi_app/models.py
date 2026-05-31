from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import declarative_base
from database import engine

base= declarative_base()

class usr(base):
    __tablenames__= "usrs"

    id = Column(Integer, primary_key=True)
    usrname= Column(String(50), unique=True)
    email= Column(String(50), unique=True)
    pwd_hash= Column(String)
    created_at= Column(TIMESTAMP, server_default=func.now())

base.metadata.create_all(bind=engine)