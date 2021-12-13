from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self) -> str:
        return self.name


    class Meta:
        ordering = ["-id"]


class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요.")
                                 ],
                                 help_text="예) 042-1234-1234")
    photo = models.ImageField(upload_to="shop/photo/%y/%m/%d")
    tag_set = models.ManyToManyField('tag', blank=True)


    def __str__(self) -> str:
        return f"[{self.pk}] {self.name}"


    class Meta:
        ordering = ["-id"]


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self) -> str:
        return self.name


    class Meta:
        ordering = ["name"]
