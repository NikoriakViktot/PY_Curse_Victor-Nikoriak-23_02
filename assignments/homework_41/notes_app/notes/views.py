from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Note, Category
from .forms import NoteForm

def notes_home(request):
    # --- ОБРОБКА СТВОРЕННЯ НОТАТКИ (POST) ---
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_home')
    else:
        form = NoteForm()

    # --- ОБРОБКА ПОШУКУ ТА ФІЛЬТРАЦІЇ (GET) ---
    notes = Note.objects.all().order_by('-id')

    # 1. Пошук за title
    search_query = request.GET.get('search', '')
    if search_query:
        notes = notes.filter(title__icontains=search_query)  # icontains шукає без урахування регістру

    # 2. Фільтрація за категорією
    category_id = request.GET.get('category', '')
    if category_id:
        notes = notes.filter(category_id=category_id)

    # 3. Фільтрація за часом нагадування
    reminder_filter = request.GET.get('reminder_filter', '')
    now = timezone.now()
    if reminder_filter == 'upcoming':
        notes = notes.filter(reminder__gt=now)  # Тільки майбутні нагадування
    elif reminder_filter == 'past':
        notes = notes.filter(reminder__lt=now)  # Тільки минулі нагадування
    elif reminder_filter == 'none':
        notes = notes.filter(reminder__isnull=True)  # Нотатки без нагадувань

    # Отримуємо всі категорії для відображення у списку фільтрів
    categories = Category.objects.all()

    context = {
        'notes': notes,
        'form': form,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_reminder': reminder_filter,
    }
    return render(request, 'notes_list.html', context)

# --- ФУНКЦІЯ ВИДАЛЕННЯ НОТАТКИ ---
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('notes_home')
