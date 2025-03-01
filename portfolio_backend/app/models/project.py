from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    technologies = Column(String(500))  # Comma-separated list of technologies
    github_url = Column(String(200))
    live_url = Column(String(200))
    image_url = Column(String(500))
    featured = Column(Boolean, default=False)
    order = Column(Integer, default=0)  # For custom ordering in portfolio