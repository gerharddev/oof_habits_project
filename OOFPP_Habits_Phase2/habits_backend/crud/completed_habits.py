"""This file contains the CRUD operations for the completed habits."""
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
import habits_backend.models.completed_habit as models
import habits_backend.models.habit as sub_models
import habits_backend.schemas.completed_habits as schemas


def get_by_id(db: Session, habit_id: int, skip: int = 0, limit: int = 100):
    """Get completed habits by habit_id and sort them by completed date."""
    exists = db.query(models.CompletedHabit).where(models.CompletedHabit.habit_id == habit_id).limit(1).scalar()
    if exists is None:
        return None

    query = select(models.CompletedHabit).where(models.CompletedHabit.habit_id == habit_id).order_by(
        models.CompletedHabit.completed_date).offset(
        skip).limit(
        limit)
    return db.execute(query).scalars().all()


def exist(db: Session, completed_habit: dict):
    """Check if a completed habit with these details exist."""
    q = db.query(models.CompletedHabit).filter(models.CompletedHabit.habit_id == completed_habit["habit_id"]).filter(
        models.CompletedHabit.completed_date == completed_habit["completed_date"])

    return db.query(q.exists()).scalar()


def get_by_id_detailed(db: Session, habit_id: int, skip: int = 0, limit: int = 100):
    """Get completed habits including detailed data by habit_id and sort them by completed date."""
    query = select(models.CompletedHabit).where(models.CompletedHabit.habit_id == habit_id).options(joinedload(
        models.CompletedHabit.habit).joinedload(sub_models.Habit.frequency)).order_by(
        models.CompletedHabit.completed_date).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    """Get all completed habits and sort them by habit_id and completed date."""
    query = select(models.CompletedHabit).options(joinedload(models.CompletedHabit.habit).joinedload(
        sub_models.Habit.frequency)).order_by(models.CompletedHabit.habit_id,
                                              models.CompletedHabit.completed_date).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def create(db: Session, completed_habit: schemas.CompletedHabitCreate):
    db_completed_habit = models.CompletedHabit(**completed_habit.dict())
    db.add(db_completed_habit)
    db.commit()
    db.refresh(db_completed_habit)
    return db_completed_habit


# TODO: Get correct schema
def create_list(db: Session, completed_habits: list[dict]):
    # TODO: Handle failure
    db.bulk_insert_mappings(models.CompletedHabit, completed_habits)
    db.commit()


def delete(db: Session, id: int):
    """Delete the completed habit for this id."""
    # Does an entry with this id exist
    exists = db.query(models.CompletedHabit).where(models.CompletedHabit.id == id).scalar()
    if exists is None:
        return None  # Nothing found, return None

    # Item found, delete it
    db.query(models.CompletedHabit).where(models.CompletedHabit.id == id).delete()
    db.commit()
    return "Deleted"
