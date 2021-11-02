from pydantic import BaseModel
from datetime import date
from enum import Enum

from .groups import Group


class Lesson(str, Enum):
    MATH = 'math'
    BIOLOGY = 'biology'
    PHYSICS = 'physics'
    CHEMISTRY = 'chemistry'


class BaseLecture(BaseModel):
    date: date
    lesson: Lesson
    group_id: int

    class Config:
        orm_mode = True


class Lecture(BaseLecture):
    id: int


class LectureCreate(BaseLecture):
    pass


class LectureUpdate(BaseLecture):
    pass


class LectureRepr(BaseLecture):
    date: date
    lesson: Lesson
    group: Group
