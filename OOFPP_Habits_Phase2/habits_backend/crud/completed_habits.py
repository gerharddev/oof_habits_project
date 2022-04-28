from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

import habits_backend.models.completed_habit as models
import habits_backend.models.habit as sub_models
import habits_backend.schemas.completed_habits as schemas


def get_by_id(db: Session, habit_id: int, skip: int = 0, limit: int = 100):
    query = select(models.CompletedHabit).where(models.CompletedHabit.habit_id == habit_id).options(joinedload(
        models.CompletedHabit.habit).joinedload(sub_models.Habit.frequency)).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    query = select(models.CompletedHabit).options(joinedload(models.CompletedHabit.habit).joinedload(
        sub_models.Habit.frequency)).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def create(db: Session, completed_habit: schemas.CompletedHabitCreate):
    db_completed_habit = models.CompletedHabit(**completed_habit.dict())
    db.add(db_completed_habit)
    db.commit()
    db.refresh(db_completed_habit)
    return db_completed_habit
