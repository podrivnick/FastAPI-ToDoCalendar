from abc import ABC, abstractmethod
from sqlalchemy import insert, select

from sqlalchemy.exc import NoResultFound
from configs.config_exceptions import USER_ALREADY_RELATED_WITH_CURRENT_USER
from database.database import async_session_maker
from exceptions.models_exceptions import NotFoundDataInModelByFilter, ModelsException


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def filter_model(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, new_access_user: dict) -> int:
        try:
            existing_entry = await self.filter_model(new_access_user)

            raise ValueError(USER_ALREADY_RELATED_WITH_CURRENT_USER)

        except ModelsException:
            async with async_session_maker() as session:
                stmt = insert(self.model).values(**new_access_user).returning(self.model.id)
                res = await session.execute(stmt)
                await session.commit()

                return res.scalar_one()

    async def filter_model(self, filtering_data: dict):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filtering_data)
            result = await session.execute(stmt)
            obj = result.scalars().first()

            if not obj:
                raise NotFoundDataInModelByFilter()

            return obj
