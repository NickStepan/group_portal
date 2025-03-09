from django.urls import path
from .views import diary_view, get_marks_student, migrate_users_view

urlpatterns = [
    path('student/', get_marks_student, name='diary_student'),
    #path('group/', get_marks_group, name='diary_group'),
    path('migrate-users/', migrate_users_view, name='migrate_users'), #оновити базу даних
]