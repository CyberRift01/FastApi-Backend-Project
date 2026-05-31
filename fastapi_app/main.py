import httpx
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessioLocal
from models import usr
from schema import usr_create, usr_login
from auth import password_hash, verify_password

app= FastAPI()

def get_database():
    database= SessioLocal()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def home():
    return {"message:":"API running"}

@app.post("/register.html")
def register(User:usr_create,db:Session = Depends(get_database)):
    existing= db.query(usr).filter(usr.usrname == User.usrname).first()
    if existing:
        raise HTTPException(400, "Username already exists!")
    
    new_user = usr(
                usrname=User.usrname,
                email=User.email,
                pwd_hash=password_hash(User.password)
    )

    db.add(new_user)
    db.commit()
    return {"message":"User was successfully created!"}

@app.post("/login.html")
def login(User:usr_login, db:Session = Depends(get_database)):
    db_usr= db.query(usr).filter(usr.usrname==User.usrname).first()

    if not db_usr or not verify_password(User.password,db_usr.pwd_hash):
        raise HTTPException(400, "Invalid password or username!")
    
    return {"message":"Your login was successful"}

@app.get("/rust")
async def call_rust():
    async with httpx.AsyncClient() as client:
        res = await client.get("http://actix:8081/health")
        return {"rust":res.text}
