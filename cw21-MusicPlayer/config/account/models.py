from django.db import models
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    image=models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    ACCOUNT_CHOICES = (
        ('Normal', 'NORMAL'),
        ('VIP', 'VIP'),
    )
    account_type = models.CharField(max_length=6, choices=ACCOUNT_CHOICES)
    image=models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.username

