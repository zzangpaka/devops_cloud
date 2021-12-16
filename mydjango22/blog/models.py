from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    class Meta:
        abstract = True


class Category(models.TextChoices):
    comic = "만화"
    novel = "소설"
    webnovel = "웹소설"
    webtoon = "웹툰"


class Post(TimestampedModel):
    category = models.CharField(max_length=10, choices=Category.choices, verbose_name="장르")
    author_name = models.CharField(max_length=100, verbose_name="작가")
    title = models.CharField(max_length=100, verbose_name="제목")
    photo = models.ImageField(upload_to="blog/post/%y/%m/%d", verbose_name="사진")
    description = models.TextField(verbose_name="내용")
    tag_set = models.ManyToManyField('tag', blank=True, verbose_name="태그목록")

    def __str__(self) -> str:
        return f"[{self.pk}] {self.title} {self.author_name}"

    def get_absolute_url(self) -> str:
        return reverse("blog:post_detail", args=[self.pk])


class Review(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="작품")
    author_name = models.CharField(max_length=100, verbose_name="작성자")
    title = models.CharField(max_length=100, verbose_name="제목")
    photo = models.ImageField(upload_to="blog/review/%y/%m/%d", blank=True, verbose_name="사진")
    description = models.TextField(verbose_name="내용")

    def __str__(self) -> str:
        return f"[{self.pk}] {self.title}"

    def get_absolute_url(self) -> str:
        return reverse("blog:review_detail", args=[self.pk])


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, unique=True, verbose_name="태그")

    def __str__(self) -> str:
        return self.name


class Hello(TimestampedModel):
    title = models.CharField(max_length=100, verbose_name="제목")
    photo = models.ImageField(upload_to="blog/Hello/%y/%m/%d", verbose_name="사진")
    content = models.TextField(verbose_name="내용")

    def __str__(self) -> str:
        return self.title