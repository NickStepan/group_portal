from django.urls import path, include
from .views import chek

urlpatterns = [
    path('/', chek),
]