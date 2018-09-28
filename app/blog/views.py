from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
