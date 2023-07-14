from . import views
from django.urls import path

urlpatterns=[
    path('authors/',views.author_list, name='author'),
    path('author/<int:id>', views.author_details, name='oneauthor'),
]