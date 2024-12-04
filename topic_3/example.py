from fastapi import FastAPI, Form, Query, Path
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import date

app = FastAPI()

# Basic Pydantic Model
class Author(BaseModel):
    name: str
    bio: Optional[str] = Field(None, max_length=1000, description="Author biography")
    
    # Example data using model_config
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "J.K. Rowling",
                "bio": "British author best known for Harry Potter series"
            }
        }
    }

# Nested Model
class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    publication_date: date
    price: float = Field(..., gt=0, description="Book price must be greater than 0")
    author: Author # the Author model is nested within here, showing that you can pass in nested models within models
    tags: List[str] = [] # nested python data type
    
    # Example using Field
    metadata: Dict[str, str] = Field(
        default_factory=dict,
        example={"format": "hardcover", "pages": "300"}
    )
    

# Deeply Nested Model
class Bookstore(BaseModel):
    name: str
    books: List[Book] # the Book model includes the Author model, showing that you can pass in nested models within models
    location: Dict[str, float] = Field(..., example={"lat": 40.7128, "lon": -74.0060})

# POST endpoint with request body
@app.post("/books/")
async def create_book(book: Book):
    return book

# POST with path and query parameters
@app.post("/bookstore/{store_id}/books/")
async def add_book_to_store(
    store_id: int = Path(..., gt=0),
    category: str = Query(None, min_length=3),
    book: Book = None
):
    return {"store_id": store_id, "category": category, "book": book}

# Multiple models in request
@app.post("/author/{author_id}/books/")
async def create_author_book(
    author_id: int,
    author: Author,
    book: Book
):
    return {"author_id": author_id, "author": author, "book": book}
"""
Example Request Body:
{
    "author": {
        "name": "F. Scott Fitzgerald",
        "bio": "American novelist and short story writer."
    },
    "book": {
        "title": "The Great Gatsby",
        "description": "A novel set in the Roaring Twenties.",
        "publication_date": "1925-04-10",
        "price": 10.99,
        "author": {
            "name": "F. Scott Fitzgerald",
            "bio": "American novelist and short story writer."
        },
        "tags": ["classic", "novel"],
        "metadata": {"format": "hardcover", "pages": "300"}
    }
}
Example Response:
{
    "author_id": 1,
    "author": {
        "name": "F. Scott Fitzgerald",
        "bio": "American novelist and short story writer."
    },
    "book": {
        "title": "The Great Gatsby",
        "description": "A novel set in the Roaring Twenties.",
        "publication_date": "1925-04-10",
        "price": 10.99,
        "author": {
            "name": "F. Scott Fitzgerald",
            "bio": "American novelist and short story writer."
        },
        "tags": ["classic", "novel"],
        "metadata": {"format": "hardcover", "pages": "300"}
    }
}
Test with:
http POST "http://localhost:8000/author/1/books/" author:='{
    "name": "F. Scott Fitzgerald",
    "bio": "American novelist and short story writer."
}' book:='{
    "title": "The Great Gatsby",
    "description": "A novel set in the Roaring Twenties.",
    "publication_date": "1925-04-10",
    "price": 10.99,
    "author": {
        "name": "F. Scott Fitzgerald",
        "bio": "American novelist and short story writer."
    },
    "tags": ["classic", "novel"],
    "metadata": {"format": "hardcover", "pages": "300"}
}'
"""

# Form data submission
@app.post("/books/form/")
async def create_book_form(
    title: str = Form(..., description="The title of the book"),
    author_name: str = Form(..., description="The name of the author"),
    price: float = Form(..., gt=0, description="The price of the book, must be greater than 0")
):
    return {
        "title": title,
        "author_name": author_name,
        "price": price
    }

"""
Run with uvicorn example:app --reload
Visit http://localhost:8000/docs for interactive documentation

Example tests
# Request with path parameter only
curl -X POST "http://localhost:8000/bookstore/1/books/" -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "description": "A novel set in the Roaring Twenties.", "publication_date": "1925-04-10", "price": 10.99, "author": {"name": "F. Scott Fitzgerald", "bio": "American novelist and short story writer."}, "tags": ["classic", "novel"], "metadata": {"format": "hardcover", "pages": "300"}}'

# Request with path and query parameters
curl -X POST "http://localhost:8000/bookstore/1/books/?category=fiction" -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "description": "A novel set in the Roaring Twenties.", "publication_date": "1925-04-10", "price": 10.99, "author": {"name": "F. Scott Fitzgerald", "bio": "American novelist and short story writer."}, "tags": ["classic", "novel"], "metadata": {"format": "hardcover", "pages": "300"}}'


# Request with path parameter only
http POST "http://localhost:8000/bookstore/1/books/" title="The Great Gatsby" description="A novel set in the Roaring Twenties." publication_date="1925-04-10" price:=10.99 author:='{"name": "F. Scott Fitzgerald", "bio": "American novelist and short story writer."}' tags:='["classic", "novel"]' metadata:='{"format": "hardcover", "pages": "300"}'

# Request with path and query parameters
http POST "http://localhost:8000/bookstore/1/books/?category=fiction" title="The Great Gatsby" description="A novel set in the Roaring Twenties." publication_date="1925-04-10" price:=10.99 author:='{"name": "F. Scott Fitzgerald", "bio": "American novelist and short story writer."}' tags:='["classic", "novel"]' metadata:='{"format": "hardcover", "pages": "300"}'

"""
