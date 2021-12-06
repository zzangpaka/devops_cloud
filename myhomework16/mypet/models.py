from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Type(models.TextChoices):
    Male = "남자"
    Female = "여자"


class MyPet(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    name = models.CharField(max_length=10, db_index=True, verbose_name="이름")
    gender = models.CharField(max_length=10, choices=Type.choices, default="남자", verbose_name="성별")
    neutralize = models.BooleanField(verbose_name="중성화여부")
    content = models.TextField(verbose_name="내용")
    photo = models.ImageField(verbose_name="사진")
    thumbnail = ImageSpecField(
        source="photo",
        processors=[ResizeToFill(1000, 600)],
        format="JPEG",
        options={"quality": 70},
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    def __str__(self) -> str:
        return self.title