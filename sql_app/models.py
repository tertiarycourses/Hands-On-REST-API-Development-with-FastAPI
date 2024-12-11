from sqlalchemy import Column, Integer, String

from .database import Base # base object is from database.py where we used declarative_base() to create a base object

class Film(Base): # model class inherits from the base class
    __tablename__ = "films"
    
    id = Column(Integer, primary_key=True, index=True) # primary key for the table
    name = Column(String, unique=True)
    director = Column(String)