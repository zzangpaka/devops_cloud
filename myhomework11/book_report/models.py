from django.db import models
from book_report.upload_to import uuid_name_upload_to

class Type(models.TextChoices):
    Comic = "만화"
    Webtoon = "웹툰"
    Novel = "소설"
    Essay = "수필"
    Poem = "시"


class Post(models.Model):
    genre = models.CharField(
        max_length=2, choices=Type.choices, default="만화", verbose_name="장르"
    )
    author_name = models.CharField(max_length=20, verbose_name="작가 이름")
    book_name = models.CharField(max_length=100, verbose_name="책 제목")
    content = models.TextField(verbose_name="감상문")
    # upload_to
    # - 문자열 : 파일이 저장되는 폴더의 경로
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to) # 분: %M, 초: %S
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성 시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 시간")


    def __str__(self):
        return self.book_name