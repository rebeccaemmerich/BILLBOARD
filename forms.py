from django import forms

from .models import Title


class PostForm(forms.ModelForm):

    class Meta:
        model = Title
        fields = ('title', 'text', 'author')
