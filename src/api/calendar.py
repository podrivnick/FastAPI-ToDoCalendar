from fastapi import Depends, APIRouter
from typing import Annotated

from schemas.calendar import CalendarAccessSchema, AddCalendarSchema, DeleteCalendarSchema
from services.calendar import CalendarService

from models.users import User

from .dependencies.calendar import get_calendar
from .users import current_user


router = APIRouter(
    prefix="/calendar",
    tags=["Calendar"],
)


@router.post("/add_tasks")
async def add_tasks(
    data: AddCalendarSchema,
    calendar: Annotated[CalendarService, Depends(get_calendar)],
    user: User = Depends(current_user),
):
    format_data = await calendar.insert_data_to_calendar(data)
    return format_data


@router.post("/delete_tasks")
async def delete_tasks(
    data: DeleteCalendarSchema,
    calendar: Annotated[CalendarService, Depends(get_calendar)],
    user: User = Depends(current_user),
):
    deleted_task = await calendar.delete_data_from_calendar(data)

    return {'message': 'done'}
