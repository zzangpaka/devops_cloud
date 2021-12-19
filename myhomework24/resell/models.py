from django.db import models
from django.urls import reverse

from shop.models import Shop


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