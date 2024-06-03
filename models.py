from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    image_type = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Тип поста(фото)')
    type = models.CharField(max_length=200, verbose_name='Тип поста')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    date_published = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Фото')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank='True')
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={"pk":self.pk})
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank='True')
    text = models.TextField(verbose_name='Текст комментария')
    date_published = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    def __str__(self):
        return str(self.text)
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"