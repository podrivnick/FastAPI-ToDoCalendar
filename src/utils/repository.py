from abc import ABC, abstractmethod
from sqlalchemy import insert, select

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

    @abstractmethod
    async def delete_one(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, new_data: dict) -> dict:
        try:
            existing_entry = await self.filter_model(new_data)

            raise ValueError(USER_ALREADY_RELATED_WITH_CURRENT_USER)

        except ModelsException:
            async with async_session_maker() as session:
                stmt = insert(self.model).values(**new_data).returning(self.model.id)
                res = await session.execute(stmt)
                await session.commit()

                return new_data

    async def filter_model(self, filtering_data: dict):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filtering_data)
            result = await session.execute(stmt)
            obj = result.scalars().first()

            if not obj:
                raise NotFoundDataInModelByFilter()

            return obj

    async def delete_one(self, deleting_data: dict):
        try:
            existing_obj_in_db = await self.filter_model(deleting_data)

            async with async_session_maker() as session:
                await session.delete(existing_obj_in_db)
                await session.commit()
            return f'Deleted {existing_obj_in_db}'
        except ModelsException as error:
            print(error.message)
