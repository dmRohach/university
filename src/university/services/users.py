from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables
from ..models.users import User, UserCreate, UserUpdate
from university.database import get_session
from ..exceptions import NotFoundException


class UserService:
    def __init__(
            self,
            session: Session = Depends(get_session)
    ):
        self.session = session

    def _get(self, user_id: int) -> tables.User:
        user = (
            self.session.query(tables.User).filter_by(id=user_id).first()
        )
        if not user:
            raise NotFoundException()
        return user

    def get(self, user_id: int) -> User:
        return self._get(user_id)

    def create(self, user_data: UserCreate) -> tables.User:
        user = tables.User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id: int, user_data: UserUpdate) -> tables.User:
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user

    def delete(self, lecture_id: int):
        lecture = self._get(lecture_id)
        self.session.delete(lecture)
        self.session.commit()
