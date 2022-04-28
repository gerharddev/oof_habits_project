from sqlalchemy.future import select
from sqlalchemy.orm import Session
import habits_backend.models.frequency as models
import habits_backend.schemas.frequencies as schemas


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
