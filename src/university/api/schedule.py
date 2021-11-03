from datetime import date
from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from typing import List, Optional

from ..models.schedule import Schedule
from ..services.shcedule import ScheduleService
from ..services.groups import GroupService

router = APIRouter(
    prefix='/schedule'
)


@router.get('/', response_model=Schedule)
def get_schedule(
        user_id: int,
        classes_date: Optional[date] = None,
        schedule_service: ScheduleService = Depends()
):
    return schedule_service.get(classes_date=classes_date, user_id=user_id)
