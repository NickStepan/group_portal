from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from auth_system.models import CustomUser

# Create your views here.

# Представлення для сторінки профілю
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        # Отримуємо профіль за ім'ям користувача з URL
        username = self.kwargs.get('username')
        user = get_object_or_404(CustomUser, username=username)
        return get_object_or_404(UserProfile, user=user)

# Представлення для власного профілю (з обмеженням доступу)
class MyProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'userprofile/profile_detail.html'
    context_object_name = 'profile'

    
    
    def get_object(self):
        # Повертаємо профіль поточного користувача
        return self.request.user.profile
    
def get_view_profile(request, **kwargs):

        request['is_logged_in'] = request.request.user.is_authenticated
