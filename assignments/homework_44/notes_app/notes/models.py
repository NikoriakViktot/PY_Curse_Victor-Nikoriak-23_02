from django.db import models
from django.contrib.auth.models import User  # Імпортуємо модель користувача

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Note(models.Model):
    # Зв'язуємо нотатку з користувачем. Якщо користувача видаляють, видаляються і його нотатки (CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
