from models.users import User

from utils.manager import get_user_manager

from services.cookies_auth import auth_backend
from fastapi_users import fastapi_users, FastAPIUsers
from schemas.users import UserCreate
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from schemas.users import UserBase


templates = Jinja2Templates(directory="front/templates/html")

router = APIRouter()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_register_router(UserBase, UserCreate),
    prefix="/registration",
    tags=["registration"],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=False),
    prefix="/login/jwt",
    tags=["login"],
)


current_user = fastapi_users.current_user(optional=True)

