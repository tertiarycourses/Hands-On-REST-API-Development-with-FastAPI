from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/authors/", response_model=schemas.Author, status_code=status.HTTP_201_CREATED)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@app.post("/books/", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title,
        description=book.description,
        publication_date=book.publication_date,
        price=book.price,
        author_id=book.author_id,
        tags=book.tags,
        metadata=book.metadata
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Fetching Products
@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

# Deleting Products
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()
    return book

# Updating Products by ID
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

"""
Creating a Connection:
database.py sets up the connection to the SQLite database using SQLAlchemy.
engine is created to connect to the SQLite database.
SessionLocal is a session factory for creating new database sessions.
Base is the base class for all ORM models.

Creating a Model:
models.py defines the Author and Book models using SQLAlchemy.
Each model corresponds to a table in the database.
Using Table Plus:

Adding Data to Database:
example.py includes endpoints to create authors and books.
The create_author and create_book functions use SQLAlchemy to add new records to the database.
schemas.py defines the Pydantic models for request and response validation.

You can use the interactive API documentation at http://localhost:8000/docs to test the endpoints.
Add new authors and books using the provided endpoints.

Run it with:
uvicorn example:app --reload --host 0.0.0.0 --port 8000
"""