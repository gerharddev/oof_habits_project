from sqlalchemy.orm import Session, joinedload, load_only, Load, join, outerjoin
from sqlalchemy import select
from sqlalchemy.sql.expression import func

import habits_backend.models.habit as habit_models
import habits_backend.models.completed_habit as completed_models
import habits_backend.models.frequency as frequency_models
import habits_backend.schemas.habits_metadata as schemas


def is_tracked(db, habit_id):
    query = select(func.count(completed_models.CompletedHabit.id)).where(completed_models.CompletedHabit.habit_id ==
                                                                         habit_id)
    count = db.execute(query).scalar()
    return True if count > 0 else False

def get_habit_with_details(db: Session):
    # Get all the habits
    query = select(habit_models.Habit.id, habit_models.Habit.name, frequency_models.Frequency.name.label(
        "repeated")).join(habit_models.Habit.frequency)
    habits = db.execute(query).all()
    results = [(lambda h: (h, is_tracked(db, h.id)))(h) for h in habits]

    # ids = [c.customers_id for h in habits]
    # test = list(map(is_tracked(db), habits))
    # my_list = list(map(is_tracked, habits))
    # Get the metadata from completed_habits table


    return []

# all habits, flag frequency, has completed tasks
#
#     query = select(habit_models.Habit, frequency_models.Frequency).join(habit_models.Habit.frequency).options(
#         Load(habit_models.Habit).load_only(habit_models.Habit.id, habit_models.Habit.name),
#         Load(frequency_models.Frequency).load_only(frequency_models.Frequency.name))

    # query = select(habit_models.Habit.id, habit_models.Habit.name, (frequency_models.Frequency.name).label(
    #     "repeated")).join(habit_models.Habit.frequency)
    # habits = db.execute(query).all()

    # query = select(habit_models.Habit.id, habit_models.Habit.name, frequency_models.Frequency.name.label(
    #     "repeated"), func.count(completed_models.CompletedHabit.habit_id).label("tracked")).join(
    #     habit_models.Habit.frequency).outerjoin(completed_models.CompletedHabit,
    #                                             completed_models.CompletedHabit.habit_id == habit_models.Habit.id)