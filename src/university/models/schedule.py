from datetime import date
from typing import List
from pydantic import BaseModel

from .groups import Group
from .lectures import Lecture


class BaseSchedule(BaseModel):
    lectures: List[Lecture]
    group: Group

    class Config:
        orm_mode = True


class Schedule(BaseSchedule):
    pass
