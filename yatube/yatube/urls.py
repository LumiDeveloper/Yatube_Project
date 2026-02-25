from django.contrib import admin
from django.urls import path, include
from . import views
from Posts import views as posts_views 


urlpatterns = [
    path('', posts_views.index, name='index'),
    path('index/', posts_views.index, name='index'),
    path('group_list/', views.group_list, name='group_list'),


    path('admin/', admin.site.urls),
]
