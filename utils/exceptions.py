from rest_framework.serializers import ValidationError


class CustomException(Exception):
    def __init__(self, detail="Something went wrong", status_code=403):
        self.detail = detail
        self.status_code = status_code


class UnauthorizedAccessException(ValidationError):
    def __init__(self, detail="Something went wrong", status_code=403):
        self.detail = detail
        self.status_code = status_code
