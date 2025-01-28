from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
        id = models.BigAutoField(primary_key=True)
        title = models.CharField(max_length=200)
        content = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        image = models.ImageField(upload_to='posts/', null=True, blank=True)  # поле для картинки

        def __str__(self):
                return self.title

        def get_absolute_url(self):
                return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
        id = models.BigAutoField(primary_key=True)
        post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return f'Comment by {self.author.username} on {self.post.title}'
