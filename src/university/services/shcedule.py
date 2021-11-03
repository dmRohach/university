from datetime import date
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional

from university import tables
from university.database import get_session
from ..models.schedule import Schedule
from ..models.lectures import Lecture
from ..models.groups import Group


class ScheduleService:
    def __init__(
            self,
            session: Session = Depends(get_session)
    ):
        self.session = session

    def _get(self, user_id: int, classes_date: Optional[date]) -> Schedule:
        group = Group.from_orm(
            self.session.query(tables.Group).filter(tables.Group.users.any(tables.User.id == user_id)).first()
        )
        lectures = [Lecture.from_orm(lecture) for lecture in
                    self.session.query(tables.Lecture).filter_by(date=classes_date).all()
                    ]
        schedule = Schedule(lectures=lectures, group=group)
        return schedule

    def get(self, user_id: int, classes_date: Optional[date]) -> Schedule:
        return self._get(user_id, classes_date)
