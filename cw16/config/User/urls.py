from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('users/', views.user_tasks, name='users'),
    path('register/', views.register, name='userregister'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
]