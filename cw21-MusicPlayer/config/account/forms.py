from django import forms


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


CHOICES=(
    ('NORMAL', 'Normal'),
    ('VIP','VIP')
)
class UserRegisterForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    file = forms.FileField()
    account_type=forms.ChoiceField(choices = CHOICES)

