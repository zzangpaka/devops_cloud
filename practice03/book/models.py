from django.db import models


class Type(models.TextChoices):
    Comic = "만화"
    novel = "소설"


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    class Meta:
        abstract = True


class Profile(TimestampedModel):
    title = models.CharField(max_length=100, verbose_name="제목")
    photo = models.ImageField(verbose_name="사진")
    content = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "프로필"
        verbose_name_plural = "프로필"


class Book(TimestampedModel):
    genre = models.CharField(max_length=10, choices=Type.choices, default="만화", verbose_name="장르")
    author = models.CharField(max_length=20, verbose_name="작가", db_index=True)
    title = models.CharField(max_length=100, verbose_name="제목", db_index=True)
    buy = models.BooleanField(verbose_name="소장")
    content = models.TextField(verbose_name="감상")
    photo = models.ImageField(verbose_name="사진")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "독후감"
        verbose_name_plural = "독후감 목록"


class Comment(TimestampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="연관글")
    name = models.CharField(max_length=20, verbose_name="작성자")
    message = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True, verbose_name="태그")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"



