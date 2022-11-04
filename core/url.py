from django.urls import path
from . import views

urlpatterns = [
    path('login', views.index, name='login'),
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('logout', views.logout, name='logout'),
    path('likes', views.likes, name='likes'),
    
]