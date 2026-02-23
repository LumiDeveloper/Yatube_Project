from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'posts/index.html', {'posts': posts})