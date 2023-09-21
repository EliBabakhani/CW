from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import jwt
from .utils import JwtHelper
from config import settings

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
    address=models.ForeignKey(Address,null=True, on_delete=models.CASCADE)

    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []


    def get_access_token(self):
        return JwtHelper.generate_jwt_token(self.id,settings.SECRET_KEY,60)
        
    def get_refresh_token(self):
        return JwtHelper.generate_jwt_token(self.id,settings.SECRET_KEY,480)

    def __str__(self) -> str:
        return self.username
