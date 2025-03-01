from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.profile import Profile, ProfileCreate, ProfileUpdate
from app.services.profile import ProfileService
from app.middlewares.auth import get_current_user

router = APIRouter()

@router.get("/profile", response_model=Profile)
async def get_profile():
    """Get the profile information"""
    profile = await ProfileService.get_profile()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.post("/profile", response_model=Profile)
async def create_profile(
    profile: ProfileCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new profile (Admin only)"""
    return await ProfileService.create_profile(profile)

@router.put("/profile/{profile_id}", response_model=Profile)
async def update_profile(
    profile_id: int,
    profile: ProfileUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update an existing profile (Admin only)"""
    updated_profile = await ProfileService.update_profile(profile_id, profile)
    if not updated_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated_profile