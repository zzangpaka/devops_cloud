# Generated by Django 3.2.9 on 2021-11-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('G', 'Good'), ('S', 'Soso'), ('B', 'Bad')], default='G', max_length=4, verbose_name='기분')),
                ('date', models.DateField(verbose_name='날짜')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('comment', models.CharField(default=None, max_length=100, verbose_name='댓글')),
            ],
        ),
    ]
