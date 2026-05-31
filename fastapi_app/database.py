from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url= "postgresql://admin:password123@db:5432/mydb"

engine= create_engine(database_url)
SessioLocal= sessionmaker(bind=engine, autoflush=False)
