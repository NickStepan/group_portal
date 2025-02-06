from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = template_name="auth_system/register.html"
    success_url = reverse_lazy("index")

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("index")
#     else:
#         form = UserCreationForm()

#     return render(
#         request,
#         template_name="auth_system/register.html",
#         context = {"form": form}
#     )

# def login(request):
#     if request.method == "POST":
#         form =  AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("index")
#             else:
#                 messages.error(request, "Неправильний логін та пароль.")