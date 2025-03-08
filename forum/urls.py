from django.urls import path
from .views import *

urlpatterns = [
    path('', forum_home, name='forum_home'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('create/', create_topic, name='create_topic'),
]

