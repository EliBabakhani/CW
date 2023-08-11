from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.see_all_tasks, name='tasks'),
    path('details/<int:pk>', views.task_details, name='details'),
    path('cteatetask/', views.create_task, name='createtask'),
    path('search/', views.search, name='search'),
    path('result', views.search_result, name='result'),
    path('usertasks/<slug:user>', views.see_user_tasks, name='usertasks'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('update/<int:id>', views.TodoUpdateView.as_view(), name='update'),
]
