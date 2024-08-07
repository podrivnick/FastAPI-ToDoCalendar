from schemas.users import UserTokenSchema
from schemas.calendar import CalendarAssignedForSchema
from exceptions.models_exceptions import ModelsException
from exceptions.tokens_error import TokensException
from utils.check_token import check_tokens
from utils.repository import AbstractRepository


class UserService:
    def __init__(self, user: AbstractRepository):
        self.user_repo: AbstractRepository = user()

    async def filter_by_some_data_of_user(self,
                                          user_data: UserTokenSchema | CalendarAssignedForSchema,
                                          is_find_all: bool = False):
        user_data_dict = user_data.model_dump()  # get {'user_id': id, 'accessible_user_id': id}

        try:
            user_with_equal_data = await self.user_repo.filter_model(user_data_dict, is_find_all)
            return user_with_equal_data
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
