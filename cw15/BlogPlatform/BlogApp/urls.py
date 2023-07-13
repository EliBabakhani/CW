from . import views
from django.urls import path


urlpatterns=[
    path('post/',views.post_list),
    path('post/<int:pk>', views.post_details)
    ]
