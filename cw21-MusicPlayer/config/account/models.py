from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


class Artist(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    image=models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.name


class Users(AbstractUser):
    ACCOUNT_CHOICES = (
        ('Normal', 'NORMAL'),
        ('VIP', 'VIP'),
    )
    account_type = models.CharField(max_length=6, choices=ACCOUNT_CHOICES)
    image=models.ImageField(upload_to='media')
# WHY???
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='user_accounts')
    user_permissions = models.ManyToManyField(
        Permission, verbose_name='user permissions', blank=True, related_name='user_accounts_permissions'
    )

    def __str__(self) -> str:
        return self.username

