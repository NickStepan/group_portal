from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from auth_system.forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "auth_system/register.html"
    success_url = reverse_lazy("index")


class UserLoginView(LoginView):
    template_name = 'auth_system/login.html'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('task-list')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    