from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body','song')
        widgets={'body':forms.Textarea(attrs={'class':'form-control'}), 'song': forms.TextInput(attrs={'type': 'hidden'})}
