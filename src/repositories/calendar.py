from utils.repository import SQLAlchemyRepository
from models.calendar import TaskCalendar


class CalendarRepository(SQLAlchemyRepository):
    model = TaskCalendar
