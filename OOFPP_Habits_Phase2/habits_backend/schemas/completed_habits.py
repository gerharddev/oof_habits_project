from pydantic import BaseModel
from .habits import Habit
from datetime import datetime


class CompletedHabitBase(BaseModel):
    id: int
    completed_date: datetime


class CompletedHabitQuery(CompletedHabitBase):
    habit_id: int

    class Config:
        orm_mode = True


class CompletedHabitCreate(BaseModel):
    completed_date: datetime
    habit_id: int

    class Config:
        orm_mode = True


class CompletedHabit(CompletedHabitBase):
    habit: Habit

    class Config:
        orm_mode = True
