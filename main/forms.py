from django import forms
from .models import Post, Profile

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
