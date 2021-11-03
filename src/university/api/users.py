from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from typing import List

from university import tables
from ..models.users import User, UserCreate, UserUpdate
from ..services.users import UserService
from ..database import get_session


router = APIRouter(
    prefix='/user'
)


@router.get('/', response_model=List[User])
def get_users(
        session=Depends(get_session),
):
    user = (
        session
        .query(tables.User)
        .all()
    )
    return user


@router.post('/', response_model=User)
def create_user(
        user_data: UserCreate,
        user_service: UserService = Depends()
):
    return user_service.create(user_data)


@router.get('/{user_id}', response_model=User)
def get_user(
        user_id: int,
        user_service: UserService = Depends(),
):
    return user_service.get(user_id=user_id)


@router.put('/{user_id}', response_model=User)
def update_user(
        user_id: int,
        user_data: UserUpdate,
        user_service: UserService = Depends(),
):
    return user_service.update(
        user_id,
        user_data,
    )


@router.delete('/{user_id}')
def delete_user(
        user_id: int,
        user_service: UserService = Depends(),
):
    user_service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
