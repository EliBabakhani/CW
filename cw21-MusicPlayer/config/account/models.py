from django.db import models
from django.contrib.auth.models import AbstractUser
from music.models import Genre

class Artist(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    image=models.ImageField(upload_to='/media')


class User(AbstractUser):
    ACCOUNT_CHOICES = (
        ('Normal', 'NORMAL'),
        ('VIP', 'VIP'),
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_CHOICES)
    image=models.ImageField(upload_to='/media')
    interests=models.ManyToManyField(Genre)

