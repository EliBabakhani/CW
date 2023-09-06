from django.db import models
from music.models import Song
from account.models import User

class Like(models.Model):
    song=models.ForeignKey(Song, on_delete=models.CASCADE, related_name='slike')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='ulike')

class Comment(models.Model):
    body=models.TextField(null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucommnet')
    song=models.ForeignKey(Song, on_delete=models.CASCADE, related_name='scommnet')
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user}-{self.body[:30]}'
