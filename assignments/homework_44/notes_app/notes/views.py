from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Захист функцій
from django.utils import timezone
from .models import Note, Category
from .forms import NoteForm

@login_required
def notes_home(request):
    # --- ОБРОБКА СТВОРЕННЯ (POST) ---
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # commit=False дозволяє підставити користувача перед збереженням в базу
            note = form.save(commit=False)
            note.user = request.user  # Прив'язуємо нотатку до того, хто зараз увійшов
            note.save()
            return redirect('notes_home')
    else:
        form = NoteForm()

    # --- ФІЛЬТРАЦІЯ: Тільки нотатки ПОТОЧНОГО користувача ---
    notes = Note.objects.filter(user=request.user).order_by('-id')

    # Пошук за title
    search_query = request.GET.get('search', '')
    if search_query:
        notes = notes.filter(title__icontains=search_query)

    # Фільтр за категорією
    category_id = request.GET.get('category', '')
    if category_id:
        notes = notes.filter(category_id=category_id)

    # Фільтр за часом нагадування
    reminder_filter = request.GET.get('reminder_filter', '')
    now = timezone.now()
    if reminder_filter == 'upcoming':
        notes = notes.filter(reminder__gt=now)
    elif reminder_filter == 'past':
        notes = notes.filter(reminder__lt=now)
    elif reminder_filter == 'none':
        notes = notes.filter(reminder__isnull=True)

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

@login_required
def delete_note(request, note_id):
    # get_object_or_404 з перевіркою user=request.user гарантує,
    # що користувач не зможе видалити чужу нотатку, підставивши інший ID в URL
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('notes_home')
