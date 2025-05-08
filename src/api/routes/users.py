

from fastapi import APIRouter
from models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login")
async def login(user: User):
    """
    Login a user.
    """
    return {"message": "User logged in", "user": user}

@router.post("/register")
async def register(user: User):
    """
    Register a new user.
    """
    return {"message": "User registered", "user": user}

@router.post("/logout")
async def logout():
    """
    Logout a user.
    """
    return {"message": "User logged out"}

@router.get("/me")
async def get_current_user():
    """
    Get the current logged-in user.
    """
    return {"message": "Current user"}

