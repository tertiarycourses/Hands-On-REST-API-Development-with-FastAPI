"""
Pydantic Models Breakdown for FastAPI Bookstore Example
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import date

# 1. Basic Model Structure
class AuthorBreakdown:
    """
    Basic Pydantic Model Structure:
    
    class Author(BaseModel):
        name: str                            # Required string field
        bio: Optional[str] = Field(...)      # Optional string field with Field customization
        
    Key Concepts:
    - Inherits from BaseModel
    - Type annotations define field types
    - Optional[] marks non-required fields
    - Field(...) provides additional validation and metadata
    """
    
    example_author = {
        "name": "J.K. Rowling",             # Required
        "bio": "British author..."          # Optional
    }

# 2. Field Customization
class FieldExamples:
    """
    Field Customization Examples:
    
    Field(...) Parameters:
    - default: Default value if not provided
    - default_factory: Function to generate default value
    - description: Field description for documentation
    - example: Example value for documentation
    - gt/lt: Greater than/Less than validation
    - min_length/max_length: String length validation
    """
    
    field_examples = {
        "basic": Field(...),                # Required field
        "with_default": Field("Unknown"),   # Default value
        "with_validation": Field(..., min_length=1, max_length=100),
        "with_numeric": Field(..., gt=0),
        "with_description": Field(None, description="Author biography"),
        "with_example": Field(..., example={"format": "hardcover"})
    }

# 3. Nested Models
class ModelRelationships:
    """
    Nested Model Structure:
    
    Book Model contains:
    - Simple fields (title, price)
    - Complex types (publication_date)
    - Nested model (author: Author)
    - List of items (tags: List[str])
    - Dictionary (metadata: Dict[str, str])
    
    Bookstore Model demonstrates deep nesting:
    - List of nested models (books: List[Book])
    """
    
    example_structure = {
        "book": {
            "title": "str",
            "author": "Author model",
            "tags": ["str", "str"],
            "metadata": {"key": "value"}
        },
        "bookstore": {
            "name": "str",
            "books": ["Book model", "Book model"],
            "location": {"lat": "float", "lon": "float"}
        }
    }

# 4. Model Configuration
class ModelConfigExamples:
    """
    Model Configuration Options:
    
    model_config = {
        "json_schema_extra": {              # Provides example data
            "example": {...}
        }
    }
    
    Other Config Options:
    - allow_population_by_field_name
    - allow_mutation
    - validate_assignment
    """
    
    example_config = {
        "json_schema_extra": {
            "example": {
                "name": "J.K. Rowling",
                "bio": "British author..."
            }
        }
    }

# 5. Validation Flow
class ValidationExample:
    """
    Pydantic Validation Process:
    
    1. Data received as JSON/dict
    2. Type conversion attempted
    3. Validation rules applied
    4. Model instance created
    
    Example for Book:
    {
        "title": "Harry Potter"         # Validated against str, length rules
        "price": "29.99"               # Converted to float, validated > 0
        "publication_date": "2023-01-01"# Converted to date object
        "author": {...}                # Validated against Author model
    }
    """
    
    validation_steps = [
        "Receive raw data",
        "Convert types",
        "Apply validation rules",
        "Create model instance"
    ]

# 6. Usage Examples
class UsagePatterns:
    """
    Common Usage Patterns:
    
    1. Request Validation:
        @app.post("/books/")
        def create_book(book: Book):    # FastAPI validates against Book model
    
    2. Response Modeling:
        @app.get("/books/", response_model=Book)
    
    3. Model Methods:
        book_dict = book.model_dump()   # Convert to dictionary
        book_json = book.model_dump_json()  # Convert to JSON string
    """
    
    usage_examples = {
        "validation": "Automatic request validation",
        "response": "Response serialization",
        "conversion": "Data format conversion"
    }