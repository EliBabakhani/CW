from . import views
from django.urls import path


urlpatterns=[
    path('',views.home),
    path('post/',views.post_list, name='posts'),
    path('post/<int:pk>', views.post_details),
    
    ]
