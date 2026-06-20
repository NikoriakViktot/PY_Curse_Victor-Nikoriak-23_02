from django.urls import path
from .views import notes_home

urlpatterns = [
    # Залишаємо порожні лапки, щоб не додавати зайвих слів до URL
    path('', notes_home, name='notes_home'),
]
