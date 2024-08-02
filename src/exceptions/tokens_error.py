from dataclasses import dataclass

from configs.config_exceptions import TOKEN_EXCEPTION, TOKEN_USER_EQUAL_TOKEN_IN_REQUEST


@dataclass
class TokensException(Exception):
    @property
    def message(self):
        return TOKEN_EXCEPTION


@dataclass
class TokenUserEqualTokenInRequest(TokensException):
    @property
    def message(self):
        return TOKEN_USER_EQUAL_TOKEN_IN_REQUEST

