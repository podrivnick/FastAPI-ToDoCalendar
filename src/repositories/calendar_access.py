from models.users import CalendarAccess
from utils.repository import SQLAlchemyRepository


class CalendarAccessRepository(SQLAlchemyRepository):
    model = CalendarAccess
