from .base_api_exception import BaseApiException


class TwoFactorCodeRequiredException(BaseApiException): 

    def __init__(self, message: str = "Two factor code required"):
        super().__init__(message=message, status=400)