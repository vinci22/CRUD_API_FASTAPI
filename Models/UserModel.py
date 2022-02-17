from xmlrpc.client import Boolean
from sqlalchemy import ForeignKey,Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from Config.db import engine,metadata

users = Table("users",metadata,
Column("id",Integer),
Column("Name",String(255)),
Column("email",String(255)),
Column("password",String(255)),
Column("status",Boolean),
Column("ip",String(255))
)

