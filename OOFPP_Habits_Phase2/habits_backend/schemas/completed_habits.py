from pydantic import BaseModel
from .habits import Habit
from datetime import datetime


class CompletedHabitBase(BaseModel):
    completed_date: datetime


class CompletedHabitCreate(CompletedHabitBase):
    habit_id: int

    class Config:
        orm_mode = True


class CompletedHabit(CompletedHabitBase):
    id: int
    habit: Habit

    class Config:
        orm_mode = True
