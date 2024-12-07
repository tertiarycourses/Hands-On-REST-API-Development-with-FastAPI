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
        from_attributes = True  # Updated from orm_mode to from_attributes

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    publication_date: date
    price: float
    author_id: int
    tags: Optional[str] = None
    extra_metadata: Optional[str] = None 

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True  # Updated

# Authentication classes
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # Updated
