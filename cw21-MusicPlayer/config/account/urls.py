from django.urls import path
from account import views


app_name='account'
urlpatterns = [
    path('login',views.UserLoginView.as_view(), name='user_login'),
    path('register', views.UserRegisterView.as_view(), name='user_register'),
    path('logout', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/<int:id>', views.UserProfileView.as_view(), name='user_profile'),
]