from pydantic import BaseModel, EmailStr

class usr_create(BaseModel):
    usrname:str
    email:str
    password:str

class usr_login(BaseModel):
    usrname:str
    password:str
