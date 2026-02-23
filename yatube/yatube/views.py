from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    return render(request, template)

def ice_cream_list(request):
    return HttpResponse('Список мороженого')

def ice_cream_detail(request, pk):
    try:
        return HttpResponse(f'Мороженое номер {pk}')
    except Exception as e:
        return HttpResponse(f'Ошибка запроса: {e}')