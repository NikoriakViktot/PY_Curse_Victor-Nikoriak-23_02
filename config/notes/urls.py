from django.urls import path
from . import views

# Додаємо назву простору імен, щоб Django не плутав посилання
app_name = 'notes'

urlpatterns = [
    # Тепер головна сторінка додатка показуватиме список нотаток
    path('', views.home, name='home'),

    # Створення нотатки тепер буде за адресою /notes/create/
    path('create/', views.note_create, name='note_create'),

    # Сторінка деталей/редагування та видалення залишаються як були
    path('<int:pk>/', views.note_detail_edit, name='note_detail_edit'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]