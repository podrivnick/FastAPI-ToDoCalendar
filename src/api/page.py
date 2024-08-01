from fastapi import APIRouter, Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_async_session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from models.users import User, CalendarAccess
from utils.filtering_user import FilteringUser

from .users import current_user


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
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session)
) -> HTMLResponse:
    db_calendar_access = []
    if user:
        filter_user_by_access_calendar = FilteringUser(db)
        db_calendar_access = await filter_user_by_access_calendar.filter_by_calendar_access(user.id)

    return templates.TemplateResponse("index.html", {
                                                     "request": request,
                                                     "user": user,
                                                     "db_calendar_access": db_calendar_access,
                                                     }
                                      )

