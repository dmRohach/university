from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from typing import List

from ..models.groups import Group, GroupCreate, GroupUpdate
from ..services.groups import GroupService


router = APIRouter(
    prefix='/groups'
)


@router.post('/', response_model=Group)
def create_group(
        group_data: GroupCreate,
        group_service: GroupService = Depends()
):
    return group_service.create(group_data)


@router.get('/', response_model=List[Group])
def get_group_list(
        group_id: int = None,
        group_service: GroupService = Depends()
):
    return group_service.get_list(number=group_id)


@router.get('/{group_id}', response_model=Group)
def get_group(
        group_id: int,
        group_service: GroupService = Depends()
):
    return group_service.get(group_id=group_id)


@router.put('/{group_id}', response_model=Group)
def update_group(
        group_id: int,
        group_data: GroupUpdate,
        lecture_service: GroupService = Depends(),
):
    return lecture_service.update(
        group_id,
        group_data,
    )


@router.delete('/{group_id}')
def delete_group(
        group_id: int,
        group_service: GroupService = Depends(),
):
    group_service.delete(group_id,)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
