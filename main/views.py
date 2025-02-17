from django.http import HttpRequest
from django.shortcuts import render

from utils import get_cookie_data


def index(request: HttpRequest):

    resp = render(request, 'base.html', context={'cookies': get_cookie_data(request)})
    print(resp.content)
    return resp
