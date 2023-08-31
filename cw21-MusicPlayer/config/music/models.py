from django.db import models
from account.models import Artist,Users

class Genre(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=100)
    artist=models.ManyToManyField(Artist)
    upload_at=models.DateTimeField(auto_now=True)
    cover_photo=models.ImageField()
    audio_file=models.FileField(upload_to="uploads/%Y/%m/")
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    

class PlayList(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    owner=models.ForeignKey(Users,on_delete=models.CASCADE)
    song=models.ManyToManyField(Song)

    def __str__(self) -> str:
        return self.title
