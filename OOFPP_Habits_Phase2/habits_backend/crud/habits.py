from sqlalchemy.orm import Session

from habits_backend.models import habits
from habits_backend.schemas.habits import *


def get_habit(db: Session, habit_id: int):
    return db.query(habits.Habit).filter(habits.Habit.id == habit_id).first()


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(habits.Habit).offset(skip).limit(limit).all()


def create_habit(db: Session, habit: HabitCreate):
    db_user = habits.Habit(name=habit.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
