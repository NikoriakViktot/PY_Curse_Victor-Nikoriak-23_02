from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
import time
import asyncio

# --- Твої робочі синхронні views (залишаємо як було) ---

@login_required
def home(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'home.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes:home')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_detail_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('notes:home')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


# --- ДЛЯ ДОМАШКИ: Ендпоінти для тестування швидкості ---

# 1. СИНХРОННИЙ ТЕСТ (імітує затримку 0.2 секунди)
def sync_test_view(request):
    time.sleep(0.2)  # Блокує весь потік на 0.2 сек
    return HttpResponse("Синхронна відповідь")

# 2. АСИНХРОННИЙ ТЕСТ (імітує затримку 0.2 секунди)
async def async_test_view(request):
    await asyncio.sleep(0.2)  # Не блокує потік під час очікування
    return HttpResponse("Асинхронна відповідь")