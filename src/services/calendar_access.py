from schemas.calendar import CalendarAccessSchema
from utils.repository import AbstractRepository


class CalendarAccessService:
    def __init__(self, calendar_access: AbstractRepository):
        self.calendar_access: AbstractRepository = calendar_access()

    async def add_access(self, calendar_access_data: CalendarAccessSchema):
        calendar_access_dict = calendar_access_data.model_dump()  # get {'user_id': id, 'accessible_user_id': id}
        calendar_access_id = await self.calendar_access.add_one(calendar_access_dict)
        return calendar_access_id
