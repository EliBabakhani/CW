from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'tags', 'status_field']
    

class MyTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('description','title',)


class ProfileForm(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    image=forms.ImageField()

