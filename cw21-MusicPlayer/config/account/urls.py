from django.urls import path
from account import views

urlpatterns = [
    path('login',views.index, name='ind')
]