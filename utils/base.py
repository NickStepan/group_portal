from django.http import HttpRequest
from .data import UserData


def get_user_data(request: HttpRequest) -> UserData:
    user = request.user.settings
    return UserData(theme=user.get('theme', 'light'))
