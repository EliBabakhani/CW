from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Song

class SongListView(ListView):
    model=Song
    template_name='music/all_songs.html'

class SongDetailView(DetailView):
    model=Song
    template_name='music/song.html'
    pk_url_kwarg = 'pk'
