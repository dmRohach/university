from fastapi import APIRouter
from .users import router as users_router
from .lectures import router as lectures_router
from .groups import router as group_router
from .schedule import router as schedule_router


router = APIRouter()
router.include_router(users_router)
router.include_router(lectures_router)
router.include_router(group_router)
router.include_router(schedule_router)
