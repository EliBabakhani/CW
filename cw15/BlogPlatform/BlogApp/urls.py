from . import views
from django.urls import path



urlpatterns=[
    path('',views.home, name='home'),
    path('posts/',views.post_list, name='posts'),
    path('post/<int:pk>', views.post_details, name='my'),
    path('categories/', views.category_list, name='categories'),
    path('category/<int:pk>', views.category_list, name='category'),

    ]
