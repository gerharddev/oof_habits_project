from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
import habits_backend.models.habit as models
import habits_backend.models.frequency as frequency_model
import habits_backend.schemas.habits as schemas


def get_habit_by_id(db: Session, habit_id: int):
    query = select(models.Habit).where(models.Habit.id == habit_id).options(joinedload(models.Habit.frequency)).limit(1)
    return db.execute(query).scalar()


def get_habit_by_name(db: Session, name: str):
    return db.query(models.Habit).filter(models.Habit.name == name).first()


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    query = select(models.Habit).options(joinedload(models.Habit.frequency)).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def get_habits_ids(db: Session):
    query = select(models.Habit.id)
    return db.execute(query).scalars().all()


def get_frequency(db: Session, habit_id: int):
    query = select(frequency_model.Frequency.repeat).where(models.Habit.id == habit_id).join(
        models.Habit.frequency).limit(1)
    return db.execute(query).scalar()


def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(**habit.dict())
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


def create_habits(db: Session, habits: list[dict]):
    # Check if values exist, and do not re-insert
    # db.query(models.Habit).delete()
    # db.commit()
    # db.add_all(models.Habit, habits)
    if len(habits) <= 0:
        return
    db.bulk_insert_mappings(models.Habit, habits)
    db.commit()


def delete(db: Session, id: int):
    """Delete the Habit with all the completed habits."""
    # Does the habit exist
    exists = db.query(models.Habit).where(models.Habit.id == id).scalar()
    if exists is None:
        return None  # Nothing found, return None
    # TODO: Delete all completed habits also
    # Item found, delete it
    db.query(models.Habit).where(models.Habit.id == id).delete()
    db.commit()
    return "Deleted"
