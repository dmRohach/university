from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str = Field(..., max_length=15)
    group_id: int


class UserCreate(BaseUser):
    pass


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(BaseUser):
    pass
