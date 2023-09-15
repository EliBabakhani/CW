from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Address:
    address=models.CharField(max_length=200)


class User(AbstractBaseUser):
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)