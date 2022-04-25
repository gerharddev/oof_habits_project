from enum import Enum
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


class TimeCode(str, Enum):
    day = 'day'
    week = 'week'
    month = 'month'
    year = 'year'


class FrequencyBase(BaseModel):
    name: str
    repeat: TimeCode  # FrequencyBase.repeat = TF.day

    class Config:
        use_enum_values = True


class FrequencyCreate(FrequencyBase):
    pass


class Frequency(FrequencyBase):
    id: int

    class Config:
        orm_mode = True
