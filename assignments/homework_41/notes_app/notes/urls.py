from django.urls import path
from .views import notes_home, delete_note

urlpatterns = [
    path('', notes_home, name='notes_home'),
    path('delete/<int:note_id>/', delete_note, name='delete_note'),  # Маршрут для видалення
]
