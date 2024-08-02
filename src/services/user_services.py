from schemas.users import UserTokenSchema
from exceptions.models_exceptions import ModelsException
from exceptions.tokens_error import TokensException
from utils.check_token import check_tokens
from utils.repository import AbstractRepository


class UserService:
    def __init__(self, user: AbstractRepository):
        self.user_repo: AbstractRepository = user()

    async def filter_by_token(self, user_token_data: UserTokenSchema):
        user_token_dict = user_token_data.model_dump()  # get {'user_id': id, 'accessible_user_id': id}

        try:
            user_with_equal_token = await self.user_repo.filter_model(user_token_dict)
            return user_with_equal_token
        except ModelsException as error:
            print(error.message)

    @staticmethod
    def is_two_tokens_equal(token_current_user: str, token_in_request: str) -> bool:
        '''
        :param token_current_user: the token of the current user
        :param token_in_request: the token, which send in request
        :return: if user fill his own token - return false
        '''

        try:
            check_tokens(token_current_user, token_in_request)
            return True
        except TokensException as error:
            print(error.message)
            return False
