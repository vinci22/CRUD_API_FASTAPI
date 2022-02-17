from click import echo
from importlib_metadata import metadata
from sqlalchemy import create_engine,MetaData
engine=create_engine("mysql+pymysql://api:password@localhost:3306/Db",echo=True)
metadata=MetaData()
conn = engine.connect()