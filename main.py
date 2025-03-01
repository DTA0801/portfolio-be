from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import date
import uvicorn

app = FastAPI(
    title="Portfolio API",
    description="API for serving professional portfolio and profile information",
    version="1.0.0"
)

# Models
class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: date
    end_date: Optional[date] = None
    description: Optional[str] = None

class Experience(BaseModel):
    company: str
    position: str
    start_date: date
    end_date: Optional[date] = None
    description: str
    technologies: List[str]

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    github_url: Optional[HttpUrl] = None
    live_url: Optional[HttpUrl] = None
    image_url: Optional[HttpUrl] = None

class Skill(BaseModel):
    name: str
    category: str  # e.g., "Programming Languages", "Frameworks", "Tools"
    proficiency: int  # 1-5 scale

class SocialLink(BaseModel):
    platform: str  # e.g., "GitHub", "LinkedIn", "Twitter"
    url: HttpUrl

class Profile(BaseModel):
    name: str
    title: str
    bio: str
    location: str
    email: str
    profile_image: Optional[HttpUrl] = None
    resume_url: Optional[HttpUrl] = None
    social_links: List[SocialLink]

# Store data (in memory for now, can be replaced with database later)
profile_data = None
experiences = []
education = []
projects = []
skills = []

# Routes
@app.get("/")
async def health_check():
    return {"status": "healthy", "message": "Portfolio API is running"}

@app.get("/api/profile")
async def get_profile():
    if profile_data is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile_data

@app.post("/api/profile")
async def create_profile(profile: Profile):
    global profile_data
    profile_data = profile
    return profile

@app.get("/api/experiences")
async def get_experiences():
    return experiences

@app.post("/api/experiences")
async def add_experience(experience: Experience):
    experiences.append(experience)
    return experience

@app.get("/api/education")
async def get_education():
    return education

@app.post("/api/education")
async def add_education(edu: Education):
    education.append(edu)
    return edu

@app.get("/api/projects")
async def get_projects():
    return projects

@app.post("/api/projects")
async def add_project(project: Project):
    projects.append(project)
    return project

@app.get("/api/skills")
async def get_skills():
    return skills

@app.post("/api/skills")
async def add_skill(skill: Skill):
    skills.append(skill)
    return skill

# Optional: Get skills by category
@app.get("/api/skills/{category}")
async def get_skills_by_category(category: str):
    return [skill for skill in skills if skill.category.lower() == category.lower()]

# Optional: Get featured projects
@app.get("/api/projects/featured")
async def get_featured_projects():
    # Return the first 3 projects (you can modify this logic)
    return projects[:3] if projects else []

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)