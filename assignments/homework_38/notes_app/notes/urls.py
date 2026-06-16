from django.urls import path
from .views import hello_notes

urlpatterns = [
    path('hello/', hello_notes, name='hello_notes'),
]
