# Generated by Django 3.2.9 on 2021-11-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_report', '0005_alter_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성 시간'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 시간'),
        ),
    ]