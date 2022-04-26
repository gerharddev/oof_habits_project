"""This file is used for setting up a SQLAlchemy connection to SQLite"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine import Engine

# Set the database connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./habits_tracking.db"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False - Only required for SQLite because by default it only allows 1 thread
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# # Create a local database session
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def make_engine() -> Engine:
    return create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


def get_db() -> Session:
    """Returns a new Session on App DB"""
    session = sessionmaker(make_engine(), expire_on_commit=False)
    return session()

# def get_db() -> Session:
#     """Return a new database session"""
#     session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     return session()
