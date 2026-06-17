import time
import httpx
import asyncio

# Оновлені прямі адреси сайту:
SYNC_URL = "http://127.0.0.1:8000/global-sync/"
ASYNC_URL = "http://127.0.0.1:8000/global-async/"

def test_synchronous():
    print("--- ЗАПУСК СИНХРОННОГО ТЕСТУ ---")
    start_total = time.time()
    for i in range(1, 4):
        start_request = time.time()
        try:
            response = httpx.get(SYNC_URL)
            end_request = time.time()
            print(f"Синхронний запит №{i}: статус {response.status_code}, час: {end_request - start_request:.4f} сек")
        except Exception as e:
            print(f"Помилка синхронного запиту: Переконайся, що сервер Django запущений! ({e})")
            return
    end_total = time.time()
    print(f"Сумарний час (синхронно): {end_total - start_total:.4f}  сек\n")

async def fetch_async(client, url, number):
    start_request = time.time()
    response = await client.get(url)
    end_request = time.time()
    print(f"Асинхронний запит №{number}: статус {response.status_code}, час: {end_request - start_request:.4f} сек")
    return response

async def test_asynchronous():
    print("--- ЗАПУСК АСИНХРОННОГО ТЕСТУ ---")
    start_total = time.time()
    try:
        async with httpx.AsyncClient() as client:
            # Запускаємо 3 запити ОДНОЧАСНО
            tasks = [fetch_async(client, ASYNC_URL, i) for i in range(1, 4)]
            await asyncio.gather(*tasks)
    except Exception as e:
        print(f"Помилка асинхронного запиту: ({e})")
        return
    end_total = time.time()
    print(f"Сумарний час (асинхронно): {end_total - start_total:.4f}  сек\n")

if __name__ == "__main__":
    test_synchronous()
    asyncio.run(test_asynchronous())