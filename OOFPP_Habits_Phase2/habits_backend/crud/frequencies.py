from sqlalchemy.future import select
from sqlalchemy.orm import Session
from habits_backend.models.frequency import *
from habits_backend.schemas.frequencies import *


def get_frequencies(db: Session, skip: int = 0, limit: int = 100):
    # query = select(Frequency).order_by(Frequency.id)
    # db_frequencies = db.execute(query).scalars().all()
    # return db_frequencies
    return db.query(Frequency).offset(skip).limit(limit).all()


def get_frequency_by_name(db: Session, name: str):
    return db.query(Frequency).filter(Frequency.name == name).first()


def create_frequency(db: Session, frequency: FrequencyCreate):
    db_frequency = Frequency(**frequency.dict())
    db.add(db_frequency)
    db.commit()
    db.refresh(db_frequency)
    return db_frequency
