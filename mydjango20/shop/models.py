from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True, verbose_name="가게명")
    description = models.TextField(verbose_name="가게정보")
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     RegexValidator(r"^\d{4}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요.")
                                 ],
                                 help_text="입력예) 042-1234-1234",
                                 verbose_name="전화번호")
    photo = models.ImageField(upload_to="shop/photo/%y/%m/%d", verbose_name="사진")
    menu_set = models.ManyToManyField('menu', blank=True)
    tag_set = models.ManyToManyField('tag', blank=True)

    def __str__(self) -> str:
        return f"[{self.pk}] {self.name}"


    class Meta:
        verbose_name = "가게"
        verbose_name_plural = "가게목록"


class Menu(TimestampedModel):
    description = models.TextField(verbose_name="메뉴설명")
    photo = models.ImageField(upload_to="shop/menu/%y/%m/%d", verbose_name="메뉴사진")

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = "메뉴"
        verbose_name_plural = "메뉴목록"


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20, verbose_name="작성자")
    reorder = models.BooleanField(null=True, verbose_name="재주문의사")
    message = models.TextField(verbose_name="리뷰내용")
    photo = models.ImageField(upload_to="shop/review/%y/%m/%d",
                              blank=True,
                              verbose_name="리뷰사진")

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="태그")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그목록"