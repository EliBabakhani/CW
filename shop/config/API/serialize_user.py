from rest_framework import serializers
from account.models import User


class SerializerUser(serializers.Serializer):
    class Meta:
        model=User
        fields=['id','email','phone','username','first_name','last_name','address']

