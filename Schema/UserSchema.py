import email
from pydantic import BaseModel
from typing import Optional



class UserSchema(BaseModel):
    id:Optional[int]
    Name:str
    email:str
    password:str
    status=1
    ip:Optional[str]