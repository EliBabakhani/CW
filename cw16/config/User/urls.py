from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('users/', views.user_tasks, name='users'),
    path('register/', views.register, name='register'),
    path('login/',views.user_login, name='login'),
]