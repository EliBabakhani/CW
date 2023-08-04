from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import CustomUser


class AuthBackend(BaseBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        try:
            user=CustomUser.objects.get(username=username)


        except CustomUser.DoesNotExist:
            return None
        
        
        if user.check_password(password):
            return user

    
