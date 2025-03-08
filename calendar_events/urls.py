from django.urls import path
from .views import calendar_redirect, calendar_view, day_view, add_event, delete_event, mark_completed

urlpatterns = [
    path('', calendar_redirect, name='calendar_redirect'),
    path('<int:year>/<int:month>/', calendar_view, name='calendar_by_month'),
    path('<int:year>/<int:month>/<int:day>/', day_view, name='calendar_by_day'),
    path('add/', add_event, name='add_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('mark_completed/<int:event_id>/', mark_completed, name='mark_completed'),
]
