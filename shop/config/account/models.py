from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Address(models.Model):
    address=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.address


class User(AbstractBaseUser):
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    address=models.ForeignKey(Address,null=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username
