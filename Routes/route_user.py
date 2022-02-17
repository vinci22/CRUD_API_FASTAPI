

from select import select
from fastapi import APIRouter,Request
from sqlalchemy import delete
from cryptography.fernet import Fernet
from Config.db import metadata,conn
from Models.UserModel import users
from Schema.UserSchema import UserSchema 

user_route = APIRouter()
"""
Definicion de endpoint para users

"""

@user_route.post("/create")
async def CreateUser(data:UserSchema,req:Request):
    user_ip=req.client.host
    newUser = {"Name":data.Name,"email":data.email,"password":data.password,"status":data.status,"ip":user_ip}
    conn.execute(users.insert().values(newUser))
    response = conn.execute(users.select().where(users.c.id == data.id))
    return f"{data.Name} tu usuario se creo con exito, bienvenido!! desde la ip{user_ip}"

@user_route.put("/delete/{id}")
async def DeleteUser(id: int,status:bool)->str:
    
    query=conn.execute(users.update().where(users.c.id == id).values({"status":status}))
    user_delete=conn.execute(users.select(users.c.Name).where(users.c.id == id))
    return "eliminado"

@user_route.put("/update/{id}")
async def UpdateUser(id:int)->str:
    
    pass

@user_route.get("/user/{id}")
async def GetUser(id:int)->str:
    UsersQuery=conn.execute(users.select().where(users.c.id==id)).fetchall()
    return UsersQuery  

@user_route.get("/users")
async def GetUsers()->str:
    UsersQuery=conn.execute(users.select()).fetchall()
    return UsersQuery  

