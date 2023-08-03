from django.forms import ModelForm, CharField, PasswordInput
from .models import CustomUser


class UserForm(ModelForm):
    passwordconfirm=CharField(widget=PasswordInput)
    class Meta:
        model=CustomUser
        fields=('username', 'email', 'password')