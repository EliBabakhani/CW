from typing import Any, Dict
from django import http
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import DetailView, ListView,View
from .models import Song, PlayList
from comment.models import Like,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePlaylistForm, AddtoPlaylistForm
from comment.forms import CreateCommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from django.http import JsonResponse

class SongListView(ListView):
    model=Song
    template_name='music/all_songs.html'


# class SongDetailsView(View):
#     form_class = CreateCommentForm
    
#     def setup(self, request, *args: Any, **kwargs: Any) -> None:
#         self.song_instance= Song.objects.get(pk=kwargs['song_id'])
#         return super().setup(request, *args, **kwargs)

#     def get(self, request):
#         playlists = PlayList.objects.filter(owner=request.user.id)
#         comments = Comment.objects.filter(song=self.song_instance)
#         form = self.form_class()
        
#         return render(request, 'music/song.html', {'form': form, 'comments': comments, 'playlists': playlists})
   
#     @method_decorator(login_required)
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.song = self.song_instance
#             comment.save()
#             messages.success(request, 'Commented successfully', 'success')
#             return redirect('music:song',self.song_instance.id)

#         playlists = PlayList.objects.filter(owner=request.user.id)
#         comments = Comment.objects.filter(song=self.song_instance)

#         return render(request, 'music/song.html', {'form': form, 'comments': comments, 'playlists': playlists})



# class SongDetailsView(View):
#     form_class=CreateCommentForm

#     def setup(self, request, *args: Any, **kwargs: Any) -> None:
#         self.song_instance=Song.objects.get(id=kwargs['song_id'])
#         return super().setup(request, *args, **kwargs)

#     def get(self, request):
#         playlists=PlayList.objects.filter(owner=self.request.user.id)
#         commnet=Comment.objects.filter(song=self.song_instance)
#         form=self.form_class
#         return render(request,'music/song.html',{'form':form, 'comment':commnet, 'playlists':playlists})
    
#     def post(self, request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             comment=form.save(commit=False)
#             comment.user=request.user
#             comment.song=self.song_instance
#             comment.save()
#             messages.success(request,'Commented successfully', 'success')
#             return redirect('music:song', self.song_instance.id)


class SongDetailView(DetailView):
    model=Song
    template_name='music/song.html'
    pk_url_kwarg = 'pk'

    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context= super().get_context_data(**kwargs)
        playlists=PlayList.objects.filter(owner=self.request.user.id)
        song=self.get_object()
        context['playlists']=playlists
        context['comment']=Comment.objects.filter(song=song.pk)
        context['form']=CreateCommentForm(initial={'song':song.id})
        return context


class CreateCommnetView(View):
    form_class=CreateCommentForm
    
    def post(self, request):
        if request.user.is_authenticated:
            print('is auth')
            form=self.form_class(request.POST)
            if form.is_valid():
                print('valid')
                comment=form.save(commit=False)
                comment.user=request.user
                comment.save()
                data={'comment_body':comment.body,'commnet_user': comment.user.username, 'comment_created':comment.created}
                response=JsonResponse(data)
                return response
            print('invalid')
            print(form.errors)
        print('not auth')
        response= JsonResponse({'error':'you have to log in'})
        response.status_code=403
        return response


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
        
class LikeSongView(LoginRequiredMixin, View):
    pass



