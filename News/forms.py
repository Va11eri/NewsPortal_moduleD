from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'text_post',
            'connection_categ'
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text_post = cleaned_data.get("text_post")
        if title == text_post:
            raise ValidationError('The text of the post should not be equal to the title')
        return cleaned_data
