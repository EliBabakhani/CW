from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .utils import JwtHelper
from config.settings import SECRET_KEY
from .models import User

class JwtAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header=request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise AuthenticationFailed
        prefix,token=auth_header.split()
        if not prefix=='Bearer': #front set 
            raise AuthenticationFailed
        user_id=JwtHelper.validate_jwt_token(token,SECRET_KEY)
        if not user_id:
            raise AuthenticationFailed
        user=User.objects.get(id=user_id)
        return user,token

        
            

