from django.urls import path
from . import views

urlpatterns = [
    path("create_users/", views.create_users, name="create"),
]