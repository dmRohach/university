from datetime import date
from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from typing import List, Optional

from ..models.lectures import Lecture, Lesson, LectureCreate, LectureUpdate, LectureRepr
from ..services.lectures import LecturesService

router = APIRouter(
    prefix='/lectures'
)


@router.get('/', response_model=List[Lecture])
def get_lectures(
        lesson: Optional[Lesson] = None,
        lecture_date: Optional[date] = None,
        group_id: int = None,
        lecture_service: LecturesService = Depends()
):
    return lecture_service.get_list(lesson=lesson, lecture_date=lecture_date, group_id=group_id)


@router.post('/', response_model=Lecture)
def create_lecture(
        lecture_data: LectureCreate,
        lecture_service: LecturesService = Depends()
):
    return lecture_service.create(lecture_data)


@router.get('/{lecture_id}', response_model=Lecture)
def get_lecture(
        lecture_id: int,
        lecture_service: LecturesService = Depends(),
):
    return lecture_service.get(lecture_id)


@router.put('/{lecture_id}', response_model=Lecture)
def update_lecture(
        lecture_id: int,
        lecture_data: LectureUpdate,
        lecture_service: LecturesService = Depends(),
):
    return lecture_service.update(
        lecture_id,
        lecture_data
    )


@router.delete('/{lecture_id}')
def delete_lecture(
        lecture_id: int,
        lecture_service: LecturesService = Depends(),
):
    lecture_service.delete(lecture_id,)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
