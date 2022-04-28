"""This file contains the completed habits model declaration used for saving the data"""
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from habits_backend.database.connectors import Base


class CompletedHabit(Base):
    __tablename__ = "completed_habits"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    completed_date = Column(DateTime, nullable=False, default=datetime.utcnow, comment="Creation date in UTC")

    habit = relationship("Habit")
