from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # Добавляем поле group
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL, # Если группу удалят, пост останется (но без группы)
        blank=True,
        null=True,
        related_name='posts'
    )

    def __str__(self):
        return self.text[:15]


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название группы")
    slug = models.SlugField(unique=True, verbose_name="Адрес группы")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title
