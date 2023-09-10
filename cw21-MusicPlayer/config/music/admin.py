from django.contrib import admin
from .models import Song, PlayList, Genre

admin.site.register(Genre)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['title','upload_at']
    search_fields=['artist','title']
    list_filter=['upload_at','artist']

    



@admin.register(PlayList)
class PlylistAdmin(admin.ModelAdmin):
    list_display=['title', 'owner']
    search_fields=['title','owner']
    list_filter=['owner']


