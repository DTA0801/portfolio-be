from fastapi import FastAPI
from app.routes import profile, experience, education, project, skill
from app.middlewares.cors import setup_cors_middleware

app = FastAPI(
    title="Portfolio API",
    description="API for personal portfolio and profile viewer",
    version="1.0.0"
)

# Setup middlewares
setup_cors_middleware(app)

# Include routers
app.include_router(profile.router, prefix="/api", tags=["Profile"])
app.include_router(experience.router, prefix="/api", tags=["Experience"])
app.include_router(education.router, prefix="/api", tags=["Education"])
app.include_router(project.router, prefix="/api", tags=["Projects"])
app.include_router(skill.router, prefix="/api", tags=["Skills"])