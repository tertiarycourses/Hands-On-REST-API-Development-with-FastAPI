import pytest
from fastapi.testclient import TestClient
from example import app

client = TestClient(app)

def test_create_author():
    author_data = {
        "name": "J.K. Rowling",
        "bio": "British author best known for Harry Potter series"
    }
    response = client.post("/authors/", json=author_data)
    assert response.status_code == 201
    assert response.json()["name"] == "J.K. Rowling"

def test_create_book():
    book_data = {
        "title": "Harry Potter",
        "publication_date": "2023-01-01",
        "price": 29.99,
        "author_id": 1,
        "tags": "fantasy, magic",
        "metadata": "format: hardcover"
    }
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Harry Potter"

def test_read_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Harry Potter"

def test_update_book():
    book_data = {
        "title": "Harry Potter and the Chamber of Secrets",
        "publication_date": "2023-01-01",
        "price": 29.99,
        "author_id": 1,
        "tags": "fantasy, magic",
        "metadata": "format: hardcover"
    }
    response = client.put("/books/1", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Harry Potter and the Chamber of Secrets"

def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Harry Potter and the Chamber of Secrets"