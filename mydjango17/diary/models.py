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

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(TimestampedModel):
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "코멘트"
        verbose_name_plural = "코멘트 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"