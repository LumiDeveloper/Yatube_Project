from django.contrib import admin
from django.urls import path
from . import views
from Posts import views as posts_views 

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('morning_posts', views.morning_posts_view, name='morning_posts'),
]
