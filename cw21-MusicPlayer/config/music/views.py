from typing import Any, Dict
from django import http
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import DetailView, ListView,View
from .models import Song, PlayList
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePlaylistForm, AddtoPlaylistForm


class SongListView(ListView):
    model=Song
    template_name='music/all_songs.html'

class SongDetailView(DetailView):
    model=Song
    template_name='music/song.html'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context= super().get_context_data(**kwargs)
        playlists=PlayList.objects.all()
        context['playlists']=playlists
        return context


class CreatePlylistView(LoginRequiredMixin,View):
    form_class=CreatePlaylistForm

    def get(self, request):
        form=self.form_class()
        return render(request,'music/create_playlist.html',context={'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_playlist=form.save(commit=False)
            new_playlist.owner=request.user
            new_playlist.song=None
            new_playlist.save()
            messages.success(request,'Playlist created successfully', 'success')
            return redirect('account:user_profile')
        

class AddMusicView(LoginRequiredMixin,View):
    form_class=AddtoPlaylistForm

    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            playlist=PlayList.objects.get(id=cd['playlist_id'])
            song=Song.objects.get(id=cd['song_id'])
            playlist.song.add(song)
            messages.success(request,'Song added successfully', 'success')
            return redirect('music:song',song.id)
        return redirect('music:song',song.id)
        




