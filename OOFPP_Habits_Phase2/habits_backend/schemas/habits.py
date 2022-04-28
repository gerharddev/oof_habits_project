from pydantic import BaseModel
from .frequencies import Frequency


class HabitBase(BaseModel):
    name: str
    description: str | None = None


class HabitCreate(HabitBase):
    frequency_id: int


class Habit(HabitBase):
    id: int
    frequency: Frequency

    class Config:
        orm_mode = True
