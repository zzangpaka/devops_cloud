from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True # 추상 클래스로서 DB 테이블이 생기지 않는다 = 부모로서만 동작


class Post(TimestampedModel):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="diary/post/%y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)


class Comment(TimestampedModel):
    author_name = models.CharField(max_length=20)
    message = models.TextField()



class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)