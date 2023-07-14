from . import views
from django.urls import path


urlpatterns=[
    path('',views.home, name='home'),
    path('post/',views.post_list, name='posts'),
    path('post/<int:pk>', views.post_details, name='my'),
    path('author/',views.author_list, name='author')
    
    ]
