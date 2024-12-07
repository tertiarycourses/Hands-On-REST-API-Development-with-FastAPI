from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(String, index=True)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    publication_date = Column(Date)
    price = Column(Float)
    author_id = Column(Integer)
    tags = Column(String)
    extra_metadata = Column(String)  # Renamed from 'metadata'