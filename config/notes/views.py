from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Імпортуємо захисника сторінок
from .models import Note
from .forms import NoteForm


# 1. Головна сторінка — список нотаток ТІЛЬКИ ПОТОЧНОГО користувача
@login_required
def home(request):
    # Вибираємо з бази тільки ті нотатки, де автор — це той, хто зараз залогінений
    notes = Note.objects.filter(author=request.user)
    return render(request, 'home.html', {'notes': notes})


# 2. Створення нотатки (з автоматичним збереженням автора)
@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Кажемо Django: «Почекай зберігати в базу»
            note.author = request.user  # Сами підставляємо автора
            note.save()  # Тепер остаточно зберігаємо
            return redirect('notes:home')  # Після створення повертаємось на головну
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})


# 3. Деталі + Редагування (Тільки своєї нотатки)
@login_required
def note_detail_edit(request, pk):
    # Django знайде нотатку за ID, але ми перевіряємо, щоб її автором був поточний користувач
    note = get_object_or_404(Note, pk=pk, author=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:home')
    else:
        form = NoteForm(instance=note)

    # Зверни увагу: у тебе шаблон для деталей називається note_detail.html або note_form.html.
    # Якщо ви редагуєте в тому ж шаблоні, переконайся, що назва файлу збігається.
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})


# 4. Видалення (Тільки своєї нотатки)
@login_required
def note_delete(request, pk):
    # Знову перевіряємо, що видалити можна тільки свою нотатку
    note = get_object_or_404(Note, pk=pk, author=request.user)

    if request.method == "POST":
        note.delete()
        return redirect('notes:home')

    return render(request, 'notes/note_confirm_delete.html', {'note': note})