from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database = create_engine("sqlite:///app.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=database)
session = Session()
Base = declarative_base()


def create_db():
    Base.metadata.create_all(database)