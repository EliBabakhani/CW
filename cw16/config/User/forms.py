from django.forms import ModelForm, CharField
from .models import CustomUser


class UserForm(ModelForm):
    passwordconfirm=CharField()
    class Meta:
        model=CustomUser
        fields=('username', 'email', 'password')