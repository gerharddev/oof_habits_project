from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

import habits_backend.models.habit as models
import habits_backend.schemas.habits as schemas


def get_habit_by_id(db: Session, habit_id: int):
    query = select(models.Habit).where(models.Habit.id == habit_id).options(joinedload(models.Habit.frequency)).limit(1)
    return db.execute(query).scalar()


def get_habit_by_name(db: Session, name: str):
    return db.query(models.Habit).filter(models.Habit.name == name).first()


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    query = select(models.Habit).options(joinedload(models.Habit.frequency)).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(**habit.dict())
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit
