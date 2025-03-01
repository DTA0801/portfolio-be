from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class ProfileBase(BaseModel):
    full_name: str
    title: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    website: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    twitter: Optional[HttpUrl] = None
    profile_image: Optional[HttpUrl] = None
    resume_url: Optional[HttpUrl] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int

    class Config:
        from_attributes = True