# Generated by Django 3.2.9 on 2021-12-06 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('name', models.CharField(db_index=True, max_length=10, verbose_name='이름')),
                ('gender', models.CharField(choices=[('남자', 'Male'), ('여자', 'Female')], default='남자', max_length=2, verbose_name='성별')),
                ('neutralize', models.BooleanField(verbose_name='중성화여부')),
                ('content', models.TextField(verbose_name='내용')),
                ('photo', models.ImageField(upload_to='', verbose_name='사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mypet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypet.mypet')),
            ],
        ),
    ]
