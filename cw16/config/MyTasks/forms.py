from django import forms
from .models import Task

class TaskForm(forms.Form):
    title=forms.CharField(label='Title')
    description=forms.CharField(label='Description')
    due_date=forms.DateTimeField(label='Deadline')
    tags=forms.CharField(label='Tags')
    status_field=forms.CharField(label='Status')
    

class MyTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('description','title',)


class ProfileForm(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    image=forms.ImageField()

