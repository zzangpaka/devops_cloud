# Generated by Django 3.2.9 on 2021-12-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_alter_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
