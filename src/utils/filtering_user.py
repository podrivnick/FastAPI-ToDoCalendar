from abc import ABC, abstractmethod

from sqlalchemy.future import select
from models.users import User, CalendarAccess

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractFilteringUser(ABC):
    @abstractmethod
    async def filter_by_token(self):
        raise NotImplementedError

    @abstractmethod
    async def filter_by_calendar_access(self):
        raise NotImplementedError


class FilteringUser(AbstractFilteringUser):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def filter_by_token(self, token: str):
        # find user by token
        db_user = await self.session.execute(select(User).where(User.token == token))

        is_token_exist = db_user.scalars().first()

        return is_token_exist or None

    async def filter_by_calendar_access(self, user_id: int):

        # merge all related users in calendar
        db_calendar_access = (
            select(User)
            .join(CalendarAccess, CalendarAccess.accessible_user_id == User.id)
            .where(CalendarAccess.user_id == user_id)
        )

        result = await self.session.execute(db_calendar_access)
        calendar_access = result.scalars().all()

        return calendar_access
