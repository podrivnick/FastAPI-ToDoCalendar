from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from schemas.calendar import CalendarAccessSchema
from services.calendar_access import CalendarAccessService
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_async_session
from utils.filtering_user import FilteringUser
from models.users import User

from .dependencies.calendar_access import calendar_access_dependency
from .users import current_user

router = APIRouter(
    prefix="/calendar",
    tags=["calendar"],
)


@router.get("/add_token")
async def get_calendar(
    user_token: str,
    calendar_access: Annotated[CalendarAccessService, Depends(calendar_access_dependency)],
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session)
):
    filter_user = FilteringUser(db)
    is_token_exist = await filter_user.filter_by_token(user_token)

    if is_token_exist is None:
        raise HTTPException(status_code=404, detail="User with this token not found")

    calendar_access_schemas = CalendarAccessSchema(user_id=user.id, accessible_user_id=is_token_exist.id)
    add_access_to_calendar = await calendar_access.add_access(calendar_access_schemas)

    return {"message": "Access successfully added"}
