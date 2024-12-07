# to define the Pydantic models for request and response validation:
from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    publication_date: date
    price: float
    author_id: int
    tags: Optional[str] = None
    extra_metadata: Optional[str] = None  # Renamed from 'metadata'

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True