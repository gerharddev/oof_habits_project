"""This file contains the model declarations used for saving the data"""
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow, comment="Creation date in UTC")
    frequency_id = Column(Integer, ForeignKey("frequencies.id"))

    frequency = relationship("Frequency")


class Frequency(Base):
    __tablename__ = "frequencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    repeat = Column(String)  # day, week, month or year
