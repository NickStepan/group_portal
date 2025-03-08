from django.http import HttpRequest
from django.shortcuts import render
from utils import setup_context


def index(request: HttpRequest):
    return render(request, 'main/index.html', context=setup_context(request))
