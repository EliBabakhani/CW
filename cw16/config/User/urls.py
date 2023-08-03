from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('users/', views.user_tasks, name='users')
]