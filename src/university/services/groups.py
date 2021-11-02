from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from university.database import get_session
from .. import tables
from ..models.groups import GroupCreate, GroupUpdate, Group
from ..exceptions import NotFoundException, GroupExistsException


def get_current_group(group_id: int, session: Session = Depends(get_session)) -> Group:
    group = (
        session.query(tables.Group).filter_by(number=group_id).first()
    )
    if not group:
        raise NotFoundException()
    return group


class GroupService:
    def __init__(
            self,
            session: Session = Depends(get_session)
    ):
        self.session = session

    def _get(self, group_id: int) -> tables.Group:
        group = (
            self.session.query(tables.Group).filter_by(id=group_id).first()
        )
        if not group:
            raise NotFoundException()
        return group

    def get(self, group_id: int) -> tables.Group:
        return self._get(group_id)

    def create(self, group_data: GroupCreate) -> tables.Group:
        group = tables.Group(**group_data.dict())
        self.session.add(group)
        self.session.commit()
        return group

    def update(self, group_id: int, group_data: GroupUpdate) -> tables.Group:
        group = self._get(group_id)
        for field, value in group_data:
            setattr(group, field, value)
        try:
            self.session.commit()
        except Exception:
            raise GroupExistsException(group.number)
        return group

    def delete(self, group_id: int):
        group = self._get(group_id)
        self.session.delete(group)
        self.session.commit()

    def get_list(
            self,
            number: int = None,
    ) -> List[tables.Group]:
        query = self.session.query(tables.Group)
        if number:
            query = query.filter_by(number=number)
        groups = query.all()
        return groups
