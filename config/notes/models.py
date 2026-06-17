from django.db import models
# Підключаємо вбудовану модель користувача Django
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, default='Загальна', verbose_name="Назва категорії")

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    text = models.TextField(verbose_name="Текст нотатки")
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Нагадування")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Категорія")

    # ДОДАЄМО ЦЕ ПОЛЕ: зв'язок з користувачем
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Автор нотатки"
    )

    def __str__(self):
        return self.title