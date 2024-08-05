from schemas.calendar import CalendarAccessSchema, AddCalendarSchema, DeleteCalendarSchema
from utils.repository import AbstractRepository


class CalendarService:
    def __init__(self, calendar: AbstractRepository):
        self.calendar: AbstractRepository = calendar()

    async def insert_data_to_calendar(self, calendar_data: CalendarAccessSchema | AddCalendarSchema):
        calendar_dict = self.get_model_dump(calendar_data)  # get {'user_id': id, 'accessible_user_id': id}
        calendar_id = await self.calendar.add_one(calendar_dict)

        return calendar_id

    async def delete_data_from_calendar(self, calendar_data: DeleteCalendarSchema):
        calendar_dict = self.get_model_dump(calendar_data)  # get {'user_id': id, 'accessible_user_id': id}
        calendar_deleted_object = await self.calendar.delete_one(calendar_dict)
        return calendar_deleted_object

    @staticmethod
    def get_model_dump(calendar_data):
        return calendar_data.model_dump()
