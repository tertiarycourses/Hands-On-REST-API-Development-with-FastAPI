from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database, auth

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
        extra_metadata=book.extra_metadata  # Updated from metadata to extra_metadata
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Fetching Products
@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

# Deleting Products
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()
    return book

# Updating Products by ID
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
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

"""
Introduction to Authentication With JWT: JWTs are used to securely transmit information between parties.
Creating Login Route: The /token endpoint generates a JWT token when the user logs in with valid credentials.
Logging In the User: The authenticate_user function verifies the user's credentials.
Significance of JWT Token: JWT tokens are used to securely transmit information between parties.
Utility Function to Create JWT Token: The create_access_token function generates a JWT token with an expiration time.
Generating JWT Token: The /token endpoint generates a JWT token when the user logs in with valid credentials.
Get Current User: The get_current_user function decodes the JWT token to get the current user.
Protecting Routes: Use the Depends function to protect routes by requiring a valid JWT token.
"""