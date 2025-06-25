from fastapi import APIRouter
from .user import router as user_router
from .role import router as role_router

router = APIRouter(
    prefix="/account",
)
router.include_router(user_router)
router.include_router(role_router)