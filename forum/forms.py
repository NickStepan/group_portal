from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']