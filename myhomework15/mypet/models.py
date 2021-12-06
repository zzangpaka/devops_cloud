from django.db import models


class Type(models.TextChoices):
    Male = "남자"
    Female = "여자"


class Pet(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    name = models.CharField(max_length=10, verbose_name="이름")
    gender = models.CharField(max_length=10, choices=Type.choices, default="남자", verbose_name="성별")
    age = models.FloatField(verbose_name="나이")
    weight = models.FloatField(verbose_name="몸무게")
    neutralize = models.BooleanField(verbose_name="중성화여부")
    description = models.TextField(verbose_name="설명")
    photo = models.ImageField(verbose_name="사진")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")
