from pydantic import BaseModel


class HabitBase(BaseModel):
    name: str
    description: str | None = None


class HabitCreate(HabitBase):
    pass


class Habit(HabitBase):
    id: int
    frequency_id: int

    class Config:
        orm_mode = True
