from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND)


class GroupExistsException(HTTPException):
    def __init__(self, group_number: int) -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Group with number{group_number} already exists'
        )
