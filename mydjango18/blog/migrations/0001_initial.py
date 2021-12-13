# Generated by Django 3.2.9 on 2021-12-08 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('photo', models.ImageField(upload_to='blog/profile/%m', verbose_name='사진')),
                ('content', models.TextField(verbose_name='내용')),
            ],
            options={
                'verbose_name': '프로필',
                'verbose_name_plural': '프로필 목록',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='태그')),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그 목록',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('genre', models.CharField(choices=[('만화', 'Comic'), ('소설', 'Novel')], db_index=True, default='만화', max_length=5, verbose_name='장르')),
                ('author', models.CharField(db_index=True, max_length=20, verbose_name='작가')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='감상평')),
                ('photo', models.ImageField(blank=True, upload_to='blog/post/%y/%m/%d', verbose_name='표지사진')),
                ('tag_set', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='태그')),
            ],
            options={
                'verbose_name': '독후감',
                'verbose_name_plural': '독후감 목록',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('name', models.CharField(max_length=20, verbose_name='작성자')),
                ('comment', models.TextField(verbose_name='댓글내용')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='감상문')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글 목록',
            },
        ),
    ]