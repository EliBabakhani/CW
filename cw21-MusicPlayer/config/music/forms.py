from django import forms
from .models import PlayList


class CreatePlaylistForm(forms.ModelForm):
    class Meta:
        model=PlayList
        fields=('title','description',)

class AddtoPlaylistForm(forms.Form):
    song_id=forms.CharField()
    playlist_id=forms.CharField()