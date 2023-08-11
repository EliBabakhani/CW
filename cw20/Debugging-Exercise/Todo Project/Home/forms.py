from django import forms
from .models import Todo


class TodoForm(forms.Form):
    class Meta:
        model = Todo
        fields = ['user', 'title', 'description', 'is_completed']

class ProfileForm(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    image=forms.ImageField()

class UpdateForm(forms.Form):
    title=forms.CharField()
    desciption=forms.CharField()
