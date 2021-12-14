from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "category",
            "author_name",
            "title",
            "photo",
            "description",
        ]