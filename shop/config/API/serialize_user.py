from rest_framework import serializers
from account.models import User


class SerializerRegisterUser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','phone','username','first_name','last_name','address']
        
        def create(self, validated_data):
            password=validated_data.pop('password', None)
            instance=self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


class SerializerLogin(serializers.Serializer):

    phone = serializers.CharField(required=True, allow_null=False)


    def validate(self, data):
        phone = data.get('phone')

        if not User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError



        return data
