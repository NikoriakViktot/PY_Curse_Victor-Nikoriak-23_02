from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import time
import asyncio


# Прямо тут створюємо два чисті ендпоінти без жодного захисту
def main_sync_test(request):
    time.sleep(0.2)  # Повністю блокує потік на 0.2 сек
    return HttpResponse("Синхронно")


async def main_async_test(request):
    await asyncio.sleep(0.2)  # Відпускає потік під час очікування
    return HttpResponse("Асинхронно")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Нові прямі адреси для нашого тесту
    path('global-sync/', main_sync_test),
    path('global-async/', main_async_test),
]