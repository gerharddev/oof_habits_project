from sqlalchemy.orm import Session

from habits_backend import models
from habits_backend import schemas


def get_habit(db: Session, habit_id: int):
    return db.query(models.Habit).filter(models.Habit.id == habit_id).first()


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Habit).offset(skip).limit(limit).all()


def create_habit(db: Session, habit: schemas.HabitCreate):
    db_user = models.Habit(name=habit.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
