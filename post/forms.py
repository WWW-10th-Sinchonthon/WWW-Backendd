from django import forms
from .models import User, Post, Scrap

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'