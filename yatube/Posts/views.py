from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.utils import timezone
import datetime


def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'posts/index.html', {'posts': posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def morning_posts_view(request):
    start_date = timezone.make_aware(datetime.datetime(1854, 7, 7))
    end_date = timezone.make_aware(datetime.datetime(1854, 7, 21, 23, 59, 59))
    
    posts = Post.objects.filter(
        text__icontains='утро',
        author__username='leo',
        pub_date__range=(start_date, end_date)
    )
    
    return render(request, 'posts/index.html', {'posts': posts})