from django.http import HttpRequest
from django.shortcuts import render
from utils import get_user_data, get_cookie_data


def index(request: HttpRequest):
    return render(request, 'base.html', {
        'cookiedata': get_cookie_data(request)
    })

