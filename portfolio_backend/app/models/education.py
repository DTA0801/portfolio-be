from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String(200), nullable=False)
    degree = Column(String(200), nullable=False)
    field_of_study = Column(String(200))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    current = Column(Boolean, default=False)
    description = Column(Text)
    achievements = Column(Text)
    institution_url = Column(String(200))