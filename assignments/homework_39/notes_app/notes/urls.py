from django.urls import path
from .views import notes_list

urlpatterns = [
    path('list/', notes_list, name='notes_list'),
]
