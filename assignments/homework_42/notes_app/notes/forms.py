from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # Вказуємо поля, які користувач буде заповнювати у формі
        fields = ['title', 'text', 'reminder', 'category']

        # Додаємо красиві підписи для полів українською мовою
        labels = {
            'title': 'Заголовок нотатки',
            'text': 'Текст нотатки',
            'reminder': 'Дата та час нагадування',
            'category': 'Категорія',
        }

        # Підключаємо HTML-віджети, щоб форма виглядала акуратно
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введіть заголовок...'}),
            'text': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Напишіть щось...', 'rows': 4}),
            'reminder': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
