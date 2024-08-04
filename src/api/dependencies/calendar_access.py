from repositories.calendar_access import CalendarAccessRepository
from services.calendar import CalendarService


def calendar_access_dependency():
    return CalendarService(CalendarAccessRepository)
