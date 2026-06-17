from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),

    # ДОДАЄМО ЦЕЙ РЯДОК: він підключає готові маршрути для входу (login) та виходу (logout)
    path('accounts/', include('django.contrib.auth.urls')),
]