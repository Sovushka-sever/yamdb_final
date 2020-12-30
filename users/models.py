from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):

    ADMIN = 'admin', 'Администратор'
    MODERATOR = 'moderator', 'Модератор'
    USER = 'user', 'Пользователь'


class User(AbstractUser):
    email = models.EmailField(verbose_name='e-mail', unique=True)
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=30,
        blank=True,
        null=True,
        unique=True
    )
    bio = models.TextField(
        verbose_name='O себе',
        max_length=500,
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER,
    )
    confirmation_code = models.CharField(max_length=20, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_moderator(self):
        return self.role == UserRoles.MODERATOR
