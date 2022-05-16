from sqlalchemy.orm import Session, joinedload, load_only, Load, join, outerjoin
from sqlalchemy import select
from sqlalchemy.sql.expression import func

import habits_backend.models.habit as habit_models
import habits_backend.models.completed_habit as completed_models
import habits_backend.models.frequency as frequency_models
import habits_backend.schemas.habits_metadata as schemas


def add_tracking_count(db, habit):
    query = select(func.count(completed_models.CompletedHabit.id)).where(completed_models.CompletedHabit.habit_id ==
                                                                         habit.id)
    count = db.execute(query).scalar()
    results = habit._asdict()
    results["count"] = count

    return results


def get_habit_with_details(db: Session):
    query = select(habit_models.Habit.id, habit_models.Habit.name, frequency_models.Frequency.name.label(
        "repeated")).join(habit_models.Habit.frequency)
    habits = db.execute(query).all()
    results = [(lambda h:  add_tracking_count(db, h))(h) for h in habits]

    return results

# Get completed habits by id. Must include the date
