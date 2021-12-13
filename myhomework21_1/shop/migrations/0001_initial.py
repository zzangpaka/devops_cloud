# Generated by Django 3.2.10 on 2021-12-13 12:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('telephone', models.CharField(help_text='예) 042-1234-1234', max_length=14, validators=[django.core.validators.RegexValidator('^\\d{3}-?\\d{4}-?\\d{4}$', message='전화번호를 입력해주세요.')])),
                ('photo', models.ImageField(upload_to='shop/photo/%y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('tag_set', models.ManyToManyField(blank=True, to='shop.Tag')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]