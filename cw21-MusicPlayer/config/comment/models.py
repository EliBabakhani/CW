from django.db import models
from music.models import Song
from account.models import Users

class Like(models.Model):
    song=models.ForeignKey(Song, on_delete=models.CASCADE)
    user=models.ForeignKey(Users, on_delete=models.CASCADE)

class Comment(models.Model):
    body=models.TextField()
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    song=models.ForeignKey(Song, on_delete=models.CASCADE)
