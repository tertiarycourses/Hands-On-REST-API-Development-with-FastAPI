# run pip install fastapi uvicorn sqlalchemy sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # This line defines the URL for the SQLite database. The URL format is sqlite:///./test.db, which means the SQLite database file test.db is located in the current directory.

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # This line creates a new SQLAlchemy Engine instance. The create_engine function is used to set up the connection to the database specified by SQLALCHEMY_DATABASE_URL. The connect_args={"check_same_thread": False} argument is specific to SQLite and allows the use of the same connection across multiple threads, which is necessary for certain applications.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # This line creates a sessionmaker factory, which is a configurable factory for creating new Session objects. 
"""
autocommit=False: Disables automatic commits, meaning you need to explicitly commit transactions.
autoflush=False: Disables automatic flushing, meaning changes are not automatically written to the database until explicitly flushed or committed.
bind=engine: Binds the Session to the previously created engine, so it knows which database to connect to.
"""
Base = declarative_base() # This line creates a base class for declarative class definitions. The declarative_base function returns a new base class from which all mapped classes should inherit. This base class maintains a catalog of classes and tables relative to that base, which is used by SQLAlchemy's ORM to map Python classes to database tables.
"""
SQLAlchemy for ORM (Object-Relational Mapping) and SQLite as the database for simplicity
"""