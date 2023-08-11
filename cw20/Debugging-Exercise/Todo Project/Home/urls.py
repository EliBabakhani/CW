from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('todos/', views.TodoListView.as_view(), name='todo_list'),
    path('todos/<int:id>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('update/<int:id>', views.TodoUpdateView.as_view(), name='update'),
]
