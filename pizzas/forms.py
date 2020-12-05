from django import forms
from .models import Pizza

class CommentForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        labels = {'text': ''}