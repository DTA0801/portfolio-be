from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class SkillLevel(enum.Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"

class SkillCategory(enum.Enum):
    PROGRAMMING_LANGUAGES = "Programming Languages"
    FRAMEWORKS = "Frameworks"
    DATABASES = "Databases"
    TOOLS = "Tools"
    SOFT_SKILLS = "Soft Skills"
    OTHER = "Other"

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(SkillCategory), nullable=False)
    level = Column(Enum(SkillLevel), nullable=False)
    years_of_experience = Column(Integer)
    description = Column(String(500))
    order = Column(Integer, default=0)  # For custom ordering within category