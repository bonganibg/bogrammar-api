from fastapi import APIRouter
from src.routes import student, reviewer

# Call API Routes
router = APIRouter()
router.include_router(student.router)
router.include_router(reviewer.router)
