import pytest
from fastapi.testclient import TestClient
from datetime import date
from example import app

client = TestClient(app)

def test_create_book():
    book_data = {
        "title": "Harry Potter",
        "publication_date": "2023-01-01",
        "price": 29.99,
        "author": {
            "name": "J.K. Rowling",
            "bio": "British author"
        },
        "tags": ["fantasy", "magic"],
        "metadata": {"format": "hardcover"}
    }
    
    response = client.post("/books/", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Harry Potter"

def test_create_book_form():
    form_data = {
        "title": "Test Book",
        "author_name": "Test Author",
        "price": "19.99"
    }
    
    response = client.post("/books/form/", data=form_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"