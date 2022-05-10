from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
import habits_backend.models.frequency as models
import habits_backend.schemas.frequencies as schemas


def has_frequencies(db: Session) -> bool:
    query = select(func.count(models.Frequency.id))
    count = db.execute(query).scalar()
    return True if count > 0 else False


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


def recreate_frequencies(db: Session, frequencies: list[dict]):
    db.query(models.Frequency).delete()
    db.commit()
    for frequency in frequencies:
        db.add(models.Frequency(**frequency))
    db.commit()
