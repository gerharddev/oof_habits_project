from sqlalchemy.orm import Session

from . import models, schemas


def get_habit(db: Session, habit_id: int):
    return db.query(models.Habit).filter(models.Habit.id == habit_id).first()


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Habit).offset(skip).limit(limit).all()


# def create_habit(db: Session, habit: schemas.HabitCreate):
#     db_user = models.Habit(name=habit.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def get_frequencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Frequency).offset(skip).limit(limit).all()


def get_frequency_by_name(db: Session, name: str):
    return db.query(models.Frequency).filter(models.Frequency.name == name).first()


def create_frequency(db: Session, frequency: schemas.FrequencyCreate):
    db_frequency = models.Frequency(**frequency.dict())
    db.add(db_frequency)
    db.commit()
    db.refresh(db_frequency)
    return db_frequency
