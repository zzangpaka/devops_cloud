from django.db import models
from django.core.validators import RegexValidator


class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="가게명")
    description = models.TextField(blank=True, verbose_name="설명")
    address = models.CharField(max_length=100, verbose_name="주소")
    # TODO: GeoDjango의 PointField를 사용
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
    # TODO: 전화번호 값인지 여부를 체킹
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"^\d{3,4}-?\d{4}-?\d{4}$", message="전화번호를 입력해 주세요."),
                                 ], verbose_name="전화번호")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")


# (r"^\d(숫자){3,4}(띄어쓰기금지)-?(하이픈이 있거나 없거나. 물음표 없으면 무조건 있다.)\d{4}-?\d{4}$")