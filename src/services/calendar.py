from schemas.calendar import CalendarAccessSchema, AddCalendarSchema
from utils.repository import AbstractRepository


class CalendarService:
    def __init__(self, calendar: AbstractRepository):
        self.calendar: AbstractRepository = calendar()

    async def insert_data_to_calendar(self, calendar_data: CalendarAccessSchema | AddCalendarSchema):
        calendar_dict = calendar_data.model_dump()  # get {'user_id': id, 'accessible_user_id': id}
        calendar_id = await self.calendar.add_one(calendar_dict)

        return calendar_id
