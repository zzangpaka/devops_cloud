from django.db import models


class Today(models.TextChoices):
    GOOD = "Good"
    SOSO = "Soso"
    BAD = "Bad"


class Write(models.Model):
    mood = models.CharField(
        max_length=4, choices=Today.choices, default=Today.GOOD, verbose_name="기분"
    )
    date = models.DateField(auto_now=False, verbose_name="날짜")
    title = models.CharField(max_length=100, verbose_name="제목")
    content = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.title
