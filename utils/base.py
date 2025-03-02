from copy import deepcopy
from django.http import HttpRequest
from .data import UserData, CookieData


def get_user_data(request: HttpRequest) -> UserData:
    # user = request.user.settings
    # return UserData(theme=user.get('theme', 'light'))
    ...


def get_cookie_data(request: HttpRequest) -> CookieData:
    cookies = request.COOKIES
    return CookieData(theme=cookies.get('theme', 'light'))


def setup_context(request, context: dict | None = None) -> dict:
    cookies = {'cookies': get_cookie_data(request)}
    if context is None:
        return cookies

    context = deepcopy(context)
    context.update(cookies)

    return context
