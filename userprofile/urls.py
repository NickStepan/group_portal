from django.urls import path
from . import views
from .views import MyProfileView, ProfileDetailView

app_name = 'userprofile'

urlpatterns = [
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/my-profile', MyProfileView.as_view(), name='my_profile'),

]