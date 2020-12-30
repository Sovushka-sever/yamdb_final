from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=200)
    slug = models.SlugField(verbose_name='URL', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=200)
    slug = models.SlugField(verbose_name='URL', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название произведения', max_length=200)
    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
        validators=(MaxValueValidator(int(datetime.now().year)),),
        db_index=True
    )
    category = models.ForeignKey(
        Category,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles'
    )
    description = models.TextField(
        verbose_name='Описание', max_length=800, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
