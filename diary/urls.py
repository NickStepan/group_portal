from django.urls import path
from .views import diary_view, get_marks

urlpatterns = [
    path('diary/', get_marks, name='diary'),
]