from repositories.calendar_access import CalendarAccessRepository
from services.calendar_access import CalendarAccessService


def calendar_access_dependency():
    return CalendarAccessService(CalendarAccessRepository)
