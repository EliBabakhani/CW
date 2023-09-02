from django.shortcuts import render
from music.models import Song

def index(request):
    songs=Song.objects.all()
    return render(request,'home/index.html', context={'songs': songs})