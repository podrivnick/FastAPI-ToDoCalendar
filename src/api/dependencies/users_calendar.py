from services.user_services import UserService
from repositories.calendar import CalendarRepository


def get_users_calendar():
    return UserService(CalendarRepository)

