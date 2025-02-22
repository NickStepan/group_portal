from django.urls import path
from .views import calendar_redirect, calendar_view, day_view, add_event

urlpatterns = [
    path('', calendar_redirect, name='calendar_redirect'),  # Перенаправлення на поточний місяць
    path('<int:year>/<int:month>/', calendar_view, name='calendar_by_month'),  # Перегляд календаря
    path('<int:year>/<int:month>/<int:day>/', day_view, name='calendar_by_day'),  # Перегляд подій на день
    path('add/', add_event, name='add_event'),  # Додавання події
]
