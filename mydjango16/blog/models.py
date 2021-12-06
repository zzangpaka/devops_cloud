from django.db import models


class Post(models.Model): # pk: id (int)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 키 정의 필요 (1:N 관계에서는 N측에 fk를 심는다)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # on_delete=models.CASCADE : 포스팅삭제시 관련 댓글 자동삭제
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)