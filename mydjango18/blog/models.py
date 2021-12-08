from django.db import models


class Genre(models.TextChoices):
    comic = "만화"
    novel = "소설"


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    class Meta:
        abstract = True


class Profile(TimestampedModel):
    title = models.CharField(max_length=100, verbose_name="제목")
    photo = models.ImageField(upload_to="blog/profile/%m", verbose_name="사진")
    content = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "프로필"
        verbose_name_plural = "프로필 목록"


class Post(TimestampedModel):
    genre = models.CharField(max_length=5, choices=Genre.choices, default="만화", verbose_name="장르", db_index=True)
    author = models.CharField(max_length=20, db_index=True, verbose_name="작가")
    title = models.CharField(max_length=50, db_index=True, verbose_name="제목")
    content = models.TextField(verbose_name="감상평")
    photo = models.ImageField(upload_to="blog/post/%y/%m/%d", blank=True, verbose_name="표지사진")
    tag_set = models.ManyToManyField("Tag", blank=True, verbose_name="태그")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "독후감"
        verbose_name_plural = "독후감 목록"


class Tag(TimestampedModel):
    name = models.CharField(db_index=True, max_length=100, verbose_name="태그")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="감상문")
    name = models.CharField(max_length=20, verbose_name="작성자")
    comment = models.TextField(verbose_name="댓글내용")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"