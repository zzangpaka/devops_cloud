# Generated by Django 3.2.9 on 2021-12-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostorage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.CharField(choices=[('캐롤', 'Carol'), ('술', 'Liquor'), ('백색소음', 'Noise')], default='캐롤', max_length=4, verbose_name='분류'),
        ),
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성 시간'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail_file',
            field=models.ImageField(upload_to='', verbose_name='썸네일'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 시간'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='', verbose_name='영상'),
        ),
        migrations.AlterField(
            model_name='video',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]
