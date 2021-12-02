from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Type(models.TextChoices):
    Carol = "캐롤"
    Liquor = "술"
    Noise = "백색소음"


class Video(models.Model):
    genre = models.CharField(
        max_length=4, choices=Type.choices, default="캐롤", verbose_name="분류"
    )
    title = models.CharField(max_length=200, verbose_name="제목")
    description = models.TextField(verbose_name="내용")
    video_file = models.FileField(verbose_name="영상")
    thumbnail_file = models.ImageField(verbose_name="썸네일")
    thumbnail_file_thumb = ImageSpecField(
        source="thumbnail_file",
        processors=[ResizeToFill(800, 400)],
        format="JPEG",
        options={"quality": 60},)
    view_count = models.PositiveIntegerField(default=0, verbose_name="조회수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성 시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 시간")

    def __str__(self):
        return self.title
