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

# 1. Створення нотатки (тут тепер живе бот! 🚀)
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()  # Зберігаємо в базу сайту

            # 🔥 НАДВИЛАЄМО КОПІЮ В ТЕЛЕГРАМ!
            send_to_telegram_channel(note.title, note.text)

            return redirect('note_create')
    else:
        form = Form = NoteForm()

    notes = Note.objects.all()
    return render(request, 'notes/note_form.html', {'form': form, 'notes': notes})


# 2. Деталі + Редагування
def note_detail_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail_edit', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})


# 3. Видалення
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_create')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})