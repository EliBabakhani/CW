from django.db import models
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    image=models.ImageField(upload_to='media/images')

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    ACCOUNT_CHOICES = (
        ('N', 'NORMAL'),
        ('V', 'VIP'),
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_CHOICES)
    image=models.ImageField(upload_to='media/images')

    def __str__(self) -> str:
        return self.username

