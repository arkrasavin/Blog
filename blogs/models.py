from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    blog = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog


class BlogPost(models.Model):
    title = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_posts')
    text_blog = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text_blog[:50]}..." if len(self.text_blog) > 50 else self.text_blog
