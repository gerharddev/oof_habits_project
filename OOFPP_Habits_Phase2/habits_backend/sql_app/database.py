"""This file is used for setting up a connection to SQLite"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set the database connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./habits_tracking.db"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False - Only required for SQLite because by default it only allows 1 thread
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Create a local database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()