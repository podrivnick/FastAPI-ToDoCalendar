from fastapi import APIRouter

from schemas.calendar import CalendarSchema

router = APIRouter(
    prefix="/calendar",
    tags=["calendar"],
)


@router.get("", response_model=CalendarSchema)
async def get_calendar(
    calendar: CalendarSchema,

) -> None:
    ...

