from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=100, db_index=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="shop/photo/%y/%m/%d")
    description = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:
        return f"[{self.pk}] {self.title}"

    class Meta:
        ordering = ["-id"]

    def get_absolute_url(self) -> str:
        return reverse("shop:shop_detail", args=[self.pk])




class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Resell(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.CharField(max_length=20, db_index=True)
    parcel = models.BooleanField(null=True, verbose_name="택배비포함")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to="shop/photo/%y/%m/%d", blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-id"]

    def get_absolute_url(self) -> str:
        return reverse("shop:resell_detail", args=[self.pk])