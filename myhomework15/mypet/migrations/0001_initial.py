# Generated by Django 3.2.9 on 2021-12-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('gender', models.CharField(choices=[('남자', 'Male'), ('여자', 'Female')], default='남자', max_length=10, verbose_name='성별')),
                ('age', models.FloatField(verbose_name='나이')),
                ('weight', models.FloatField(verbose_name='몸무게')),
                ('neutralize', models.BooleanField(verbose_name='중성화여부')),
                ('description', models.TextField(verbose_name='설명')),
                ('photo', models.ImageField(upload_to='', verbose_name='사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
    ]
