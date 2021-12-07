from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    genre = models.CharField(max_length=2)
    author = models.CharField(max_length=20, db_index=True)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    message = models.TextField()


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)