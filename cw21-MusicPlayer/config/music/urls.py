from django.urls import path
from music import views


app_name='music'
urlpatterns = [
    path('songs', views.SongListView.as_view(), name='all_songs'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song'),
    path('create_playlist', views.CreatePlylistView.as_view(),name='create_playlist'),
    path('add_to_play_list/', views.AddMusicView.as_view(), name='add_to_playlist'),
    path('comments/', views.CreateCommnetView.as_view(), name='comment'),

]