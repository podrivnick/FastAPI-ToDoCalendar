from .calendar_tasks import router as calendar_router
from .users import router as users_router
from .page import router as front_router


all_routers = [
    front_router,
    users_router,
    calendar_router,
]

