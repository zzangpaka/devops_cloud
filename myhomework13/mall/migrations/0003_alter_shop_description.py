# Generated by Django 3.2.9 on 2021-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_shop_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TimeField(blank=True),
        ),
    ]
