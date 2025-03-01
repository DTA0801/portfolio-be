from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    location = Column(String(100))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    current = Column(Boolean, default=False)
    description = Column(Text)
    technologies = Column(String(500))  # Comma-separated list of technologies
    company_url = Column(String(200))