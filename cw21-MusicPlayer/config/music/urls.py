from django.urls import path
from music import views


app_name='music'
urlpatterns = [
    path('songs', views.SongListView.as_view(), name='all_songs'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song'),
    
]