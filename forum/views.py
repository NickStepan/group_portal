from django.http import HttpRequest
from django.shortcuts import render
from utils import get_user_data, get_cookie_data
from .forms import *


def index(request: HttpRequest):
    return render(request, 'base.html', {
        'cookiedata': get_cookie_data(request)
    })

def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('forum_home')
    else:
        form = TopicForm()
    return render(request, 'forum/create_topic.html', {'form': form})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comments = topic.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.author = request.user
            comment.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = CommentForm()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'comments': comments, 'form': form})

def forum_home(request):
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/home.html', {'topics': topics})