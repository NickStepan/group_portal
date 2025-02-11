from django.http import HttpRequest
from django.shortcuts import render
from utils import get_user_data, get_cookie_data
from datetime import datetime, timedelta, UTC


def index(request: HttpRequest):
    cookies = get_cookie_data(request)

    resp = render(request, 'base.html', {
        'cookies': cookies
    })

    if not request.COOKIES.get('theme'):
        resp.set_cookie("theme", "light",  expires=datetime.now(UTC) + timedelta(days=180))

    return resp
