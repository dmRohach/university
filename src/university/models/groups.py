from pydantic import BaseModel
from typing import List

from .users import User


class BaseGroup(BaseModel):
    number: int

    class Config:
        orm_mode = True


class Group(BaseGroup):
    id: int
    users: List[User]


class GroupCreate(BaseGroup):
    pass


class GroupUpdate(BaseGroup):
    pass
