from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = ""

db = create_engine(db_string)

base = declarative_base()

class Fruit(base):
    __tablename__ = 'fruits'

    name = Column(String, primary_key=True)
    color = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
