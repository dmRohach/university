from datetime import date
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from university import tables
from university.database import get_session
from ..models.lectures import LectureCreate, Lesson, LectureUpdate, Lecture
from ..exceptions import NotFoundException


def get_current_lecture(lecture_id: int, session: Session = Depends(get_session)) -> Lecture:
    lecture = (
        session.query(tables.Lecture).filter_by(id=lecture_id).first()
    )
    if not lecture:
        raise NotFoundException()
    return lecture


class LecturesService:
    def __init__(
            self,
            session: Session = Depends(get_session)
    ):
        self.session = session

    def _get(self, lecture_id: int) -> tables.Lecture:
        lecture = (
            self.session.query(tables.Lecture).filter_by(id=lecture_id).first()
        )
        if not lecture:
            raise NotFoundException()
        return lecture

    def get_list(
            self,
            lesson: Optional[Lesson] = None,
            lecture_date: Optional[date] = None,
            group_id: int = None,
    ) -> List[tables.Lecture]:
        query = self.session.query(tables.Lecture)
        if lesson:
            query = query.filter_by(lesson=lesson)
        if lecture_date:
            query = query.filter_by(date=lecture_date)
        if group_id:
            query = query.filter_by(group_id=group_id)
        lectures = query.all()
        return lectures

    def get(self, lecture_id: int) -> Lecture:
        return self._get(lecture_id)

    def create(self, lecture_data: LectureCreate) -> tables.Lecture:
        lecture = tables.Lecture(**lecture_data.dict())
        self.session.add(lecture)
        self.session.commit()
        return lecture

    def update(self, lecture_id: int, lecture_data: LectureUpdate) -> tables.Lecture:
        lecture = self._get(lecture_id)
        for field, value in lecture_data:
            setattr(lecture, field, value)
        self.session.commit()
        return lecture

    def delete(self, lecture_id: int):
        lecture = self._get(lecture_id)
        self.session.delete(lecture)
        self.session.commit()
