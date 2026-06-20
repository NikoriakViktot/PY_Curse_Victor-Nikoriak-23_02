from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)

    # ОСЬ ЦЕЙ ЗОВНІШНІЙ КЛЮЧ (Foreign Key), який пов'язує нотатку з категорією:
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
