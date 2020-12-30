from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from artworks.models import Title
from users.models import User


class Review(models.Model):
    text = models.TextField()
    score = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)
    title_id = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Дата публикации'
        verbose_name_plural = 'Даты публикации'
        unique_together = ('title_id', 'author_id')

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Дата добавления'
        verbose_name_plural = 'Даты добавления'

    def __str__(self):
        return self.text
