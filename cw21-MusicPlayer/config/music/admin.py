from django.contrib import admin
from .models import Song, PlayList, Genre

admin.site.register(Song)
admin.site.register(PlayList)
admin.site.register(Genre)

