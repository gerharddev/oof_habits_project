from enum import Enum
from pydantic import BaseModel


class TimeCode(str, Enum):
    """Define a time code to specify repetition frequency"""
    day = 'day'
    week = 'week'
    month = 'month'


class FrequencyBase(BaseModel):
    name: str
    repeat: TimeCode  # FrequencyBase.repeat = TimeCode.day

    class Config:
        use_enum_values = True


class FrequencyCreate(FrequencyBase):
    pass


class Frequency(FrequencyBase):
    id: int

    class Config:
        orm_mode = True
