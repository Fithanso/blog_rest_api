from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.TextField(verbose_name='content')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, related_name='posts',
                               verbose_name='author')
    created = models.DateTimeField(auto_now_add=True, verbose_name='create time')
    updated = models.DateTimeField(auto_now=True, verbose_name='update time')

    def __str__(self):
        return f'{self.title} by {self.author}'

    class Meta:
        db_table = 'posts'
        ordering = ['-created']


class MarkedPost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='post')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return f'{self.post} marked by {self.user}'

    class Meta:
        db_table = 'marked_posts'
        verbose_name = 'Marked post'
        verbose_name_plural = 'Marked posts'

