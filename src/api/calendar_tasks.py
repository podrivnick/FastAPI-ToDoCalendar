from fastapi import Depends, HTTPException, status, APIRouter
from typing import Annotated

from configs.config_api import EQUAL_TOKENS, ADDED_ACCESS_TO_OTHER_CALENDAR_USER, ADDED_TASKS_TO_CALENDAR

from schemas.calendar import CalendarAccessSchema, AddCalendarSchema
from services.calendar import CalendarService
from services.user_services import UserService
from schemas.users import UserTokenSchema

from models.users import User

from .dependencies.calendar_access import calendar_access_dependency
from .dependencies.user_dependencies import user_dependencies
from .users import current_user


router = APIRouter(
    prefix="/connect_calendar",
    tags=["Calendar"],
)


@router.post("/add_token")
async def connect_to_other_calendars(
    user_token: str,
    calendar_access: Annotated[CalendarService, Depends(calendar_access_dependency)],
    user_repo: Annotated[UserService, Depends(user_dependencies)],
    user: User = Depends(current_user),
):
    token_current_user = user.token
    token_request = user_token

    is_not_token_current_user_equal_request_token = user_repo.is_two_tokens_equal(token_current_user, token_request)

    if is_not_token_current_user_equal_request_token:
        user_token_schema = UserTokenSchema(token=user_token)
        user_with_equal_token = await user_repo.filter_by_some_data_of_user(user_token_schema)

        calendar_access_schemas = CalendarAccessSchema(user_id=user.id, accessible_user_id=user_with_equal_token.id)
        add_access_to_calendar = await calendar_access.insert_data_to_calendar(calendar_access_schemas)

        return {"message": ADDED_ACCESS_TO_OTHER_CALENDAR_USER}

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=EQUAL_TOKENS
        )

