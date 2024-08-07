from fastapi import APIRouter, Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_async_session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated

from services.user_services import UserService
from schemas.calendar import CalendarAssignedForSchema
from models.users import User
from utils.filtering_user import FilteringUser

from .users import current_user
from .dependencies.users_calendar import get_users_calendar

router = APIRouter(
    prefix="/page",
    tags=["page"],
)

# for local start
# templates = Jinja2Templates(directory="front/templates/html")

# for docker start
templates = Jinja2Templates(directory="src/front/templates/html")


@router.get('')
async def index(
    request: Request,
    calendar: Annotated[UserService, Depends(get_users_calendar)],
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),
) -> HTMLResponse:
    db_calendar_access = []
    filter_calendar_by_username = []
    if user:
        filter_user_by_access_calendar = FilteringUser(db)
        db_calendar_access = await filter_user_by_access_calendar.filter_by_calendar_access(user.id)

        assigned_events = CalendarAssignedForSchema(assigned_to=user.username)
        filter_calendar_by_username = await calendar.filter_by_some_data_of_user(assigned_events, is_find_all=True)

    return templates.TemplateResponse("index.html", {
                                                     "request": request,
                                                     "user": user,
                                                     "db_calendar_access": db_calendar_access,
                                                     "events": filter_calendar_by_username
                                                     }
                                      )

