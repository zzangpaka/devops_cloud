from django import forms
from blog.models import Post, Review


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"