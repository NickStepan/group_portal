from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import New

class NewsListView(ListView):
    model = New
    template_name = "news/news.html"
    context_object_name = "news"
