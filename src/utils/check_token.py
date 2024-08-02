from exceptions.tokens_error import TokenUserEqualTokenInRequest


def check_tokens(token_current_user: str, token_in_request: str):
    if token_current_user == token_in_request:
        raise TokenUserEqualTokenInRequest

