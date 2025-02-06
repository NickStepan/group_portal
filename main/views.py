from django.http import HttpRequest
from django.shortcuts import render
from utils import get_user_data


def index(request: HttpRequest):
    return render(request, 'base.html', {
        'userdata': get_user_data(request).theme
    })

