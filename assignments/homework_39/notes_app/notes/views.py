from django.shortcuts import render


def notes_list(request):
    # Тестові дані (імітація бази даних)
    mock_notes = [
        {
            'title': 'Купити продукти',
            'content': 'Молоко, хліб, сир, яблука.',
            'created_at': '15.06.2026'
        },
        {
            'title': 'ДЗ з Django',
            'content': 'Зробити виведення нотаток через HTML та CSS.',
            'created_at': '16.06.2026'
        },
        {
            'title': 'Почитати книгу',
            'content': 'Прочитати 20 сторінок про архітектуру Django.',
            'created_at': '16.06.2026'
        }
    ]

    # Передаємо дані у шаблон через контекст
    return render(request, 'notes_list.html', {'notes': mock_notes})
