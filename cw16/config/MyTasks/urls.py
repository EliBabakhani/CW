from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.AllTasksListView.as_view(), name='tasks'),
    path('details/<int:pk>', views.TaskDetailView.as_view(), name='details'),
    path('cteatetask/', views.TaskCreateView.as_view(), name='createtask'),
    path('search/', views.search, name='search'),
    path('result', views.search_result, name='result'),
    path('usertasks/<slug:user>', views.see_user_tasks, name='usertasks'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('update/<int:id>', views.TaskUpdateView.as_view(), name='update'),
]
