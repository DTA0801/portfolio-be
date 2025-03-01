from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    title = Column(String(100))
    bio = Column(Text)
    location = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    website = Column(String(200))
    github = Column(String(200))
    linkedin = Column(String(200))
    twitter = Column(String(200))
    profile_image = Column(String(500))
    resume_url = Column(String(500))