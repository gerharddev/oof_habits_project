"""Contains Habit metadata for analysis."""

from pydantic import BaseModel
from .frequencies import Frequency


class HabitMetadataBase(BaseModel):
    id: int
    name: str


class HabitMetadata(HabitMetadataBase):
    repeated: str
    count: int

    class Config:
        orm_mode = True
