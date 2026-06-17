from django.shortcuts import render, get_object_or_404, redirect
import httpx  # Використовуємо httpx для відправки запитів до Telegram
from .models import Note
from .forms import NoteForm

# ==================== НАЛАШТУВАННЯ TELEGRAM ====================
TELEGRAM_BOT_TOKEN = "8208843455:AAFSAs53mQiY53Y7kOL5i3wzSBGYAgXfRT8"
TELEGRAM_CHANNEL_ID = "@shahtarske_notes"


def send_to_telegram_channel(title, text):
    """Допоміжна функція для надсилання нотатки в Telegram-канал"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    full_message = f"📌 *Створено нову нотатку!*\n\n• *Назва:* {title}\n• *Текст:* {text}"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": full_message,
        "parse_mode": "Markdown"
    }
    try:
        response = httpx.post(url, json=payload)
        print("--- ВІДПОВІДЬ ВІД ТЕЛЕГРАМУ:", response.text, "---")
    except Exception as e:
        print(f"Не вдалося зв'язатися з Telegram: {e}")


# ==================== ТВОЇ VIEWS ====================

# 🔥 Об'єднана функція: вона і показує список, і створює нову нотатку!
def notes_list(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()  # Зберігаємо в базу сайту

            # 🚀 Відправляємо в Телеграм!
            send_to_telegram_channel(note.title, note.text)

            return redirect('notes:notes_list')
    else:
        form = NoteForm()

    notes = Note.objects.all().order_by('-created_at')
    # Передаємо форму на сторінку, щоб вона відображалася разом зі списком
    return render(request, 'notes/notes_list.html', {'notes': notes, 'form': form})


# Функція створення (залишаємо про всяк випадок, якщо потрібна для тестів курсу)
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            send_to_telegram_channel(note.title, note.text)
            return redirect('notes:notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_detail_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('notes:notes_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})