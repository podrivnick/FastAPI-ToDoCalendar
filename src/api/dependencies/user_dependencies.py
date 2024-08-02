from services.user_services import UserService
from repositories.user_repository import UserRepository


def user_dependencies():
    return UserService(UserRepository)

