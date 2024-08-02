from fastapi import APIRouter
from fastapi_users import fastapi_users, FastAPIUsers

from services.cookies_auth import auth_backend
from schemas.users import UserCreate, UserBase
from models.users import User
from utils.manager import get_user_manager


router = APIRouter()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_register_router(UserBase, UserCreate),
    prefix="/registration",
    tags=["AUTH"],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=False),
    prefix="/login/jwt",
    tags=["AUTH"],
)


current_user = fastapi_users.current_user(optional=True)
