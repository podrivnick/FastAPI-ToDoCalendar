from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from config import SECRET_KEY_AUTH as secret

SECRET = secret

cookie_transport = CookieTransport(
    cookie_name="Calendar",
    cookie_max_age=3600,
    cookie_secure=False,    # for save cookie at local host machine and docker
    cookie_samesite="Lax",  # for save cookie at local host machine and docker
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
