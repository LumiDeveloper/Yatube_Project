from django.contrib import admin
from django.urls import path
from . import views
from Posts import views as posts_views 

urlpatterns = [
    path('', posts_views.index),
    path('ice_cream/', views.ice_cream_list),
    path('ice_cream/<int:pk>/', views.ice_cream_detail),
    path('admin/', admin.site.urls),
]
