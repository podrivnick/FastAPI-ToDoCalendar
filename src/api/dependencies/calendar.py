from repositories.calendar import CalendarRepository
from services.calendar import CalendarService


def get_calendar():
    return CalendarService(CalendarRepository)

