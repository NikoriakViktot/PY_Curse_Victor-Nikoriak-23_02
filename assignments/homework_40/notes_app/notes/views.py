from django.shortcuts import render
from .models import Note


def notes_home(request):
    # Беремо всі нотатки з бази даних
    notes = Note.objects.all()

    # Вказуємо твій правильний шаблон notes_list.html
    return render(request, 'notes_list.html', {'notes': notes})
