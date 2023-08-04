from django.forms import ModelForm, CharField, PasswordInput, ValidationError, forms
from .models import CustomUser


class UserRegisterForm(ModelForm):
    confirm_password=CharField(widget=PasswordInput)
    class Meta:
        model=CustomUser
        fields=('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("password and confirm_password does not match")
        return cleaned_data

class UserLogInForm(forms.Form):
    username=CharField()
    password=PasswordInput()