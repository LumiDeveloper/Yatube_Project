from django.contrib import admin
from django.urls import path, include
from . import views
from Posts import views as posts_views 

app_name = 'group'

urlpatterns = [
    path('group_list/', views.group_list, name='group_list')
]
