from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # this points to our sqlite file that's going to be our database file

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # this is what creates a database session and bind=engine binds that session to the engine we created in earlier
# the session is then stored in the SessionLocal class and we can instantiate that class in our FastAPI endpoints when we want to create a database session

Base = declarative_base() # this is going to be used when we create a model to represent the film objects that we got in the films list in main.py
