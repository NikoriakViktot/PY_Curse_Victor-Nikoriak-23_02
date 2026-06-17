from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.note_create, name='note_create'),
    path('<int:pk>/', views.note_detail_edit, name='note_detail_edit'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),

    # Наші ендпоінти для порівняння швидкості в домашці:
    path('sync-test/', views.sync_test_view, name='sync_test'),
    path('async-test/', views.async_test_view, name='async_test'),
]