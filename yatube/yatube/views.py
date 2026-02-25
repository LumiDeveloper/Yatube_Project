from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Проект'
    context = {
        'title': title,
        'text': 'Главная страница',
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)