from django.test import TestCase
from django.urls import reverse
from .models import Note, Category


class NoteFunctionalityTests(TestCase):

    def setUp(self):
        """Налаштування початкових даних перед кожним тестом"""
        # Створюємо тестову категорію
        self.category = Category.objects.create(title="Тестова Категорія")

        # Створюємо одну тестову нотатку
        self.note = Note.objects.create(
            title="Початкова Нотатка",
            text="Початковий текст",
            category=self.category
        )

        # Отримуємо URL адреси для запитів
        self.home_url = reverse('notes_home')
        self.delete_url = reverse('delete_note', args=[self.note.id])

    def test_note_creation_via_post(self):
        """Тест збереження нової нотатки через POST-запит (Форму)"""
        # Дані, які ми нібито відправляємо з форми сайту
        data = {
            'title': 'Нова Нотатка з Тесту',
            'text': 'Текст нової тестової нотатки',
            'category': self.category.id,
            'reminder': ''  # залишаємо порожнім
        }

        # Відправляємо POST-запит на головну сторінку
        response = self.client.post(self.home_url, data)

        # Перевіряємо, чи відбувся редірект (код 302) назад на головну сторінку
        self.assertEqual(response.status_code, 302)

        # Перевіряємо, чи дійсно нотатка збереглася в базу даних
        note_exists = Note.objects.filter(title='Нова Нотатка з Тесту').exists()
        self.assertTrue(note_exists)

    def test_note_deletion(self):
        """Тест видалення нотатки через URL"""
        # Перевіряємо, що перед видаленням нотатка є в базі
        self.assertEqual(Note.objects.count(), 1)

        # Робимо запит на видалення
        response = self.client.get(self.delete_url)

        # Перевіряємо, що після видалення нас перенаправило назад
        self.assertEqual(response.status_code, 302)

        # Перевіряємо, що в базі даних більше немає цієї нотатки (кількість дорівнює 0)
        self.assertEqual(Note.objects.count(), 0)

    def test_notes_home_view_returns_correct_context(self):
        """Тест того, що сторінка успішно завантажується та віддає список нотаток"""
        response = self.client.get(self.home_url)

        # Код відповіді має бути 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Перевіряємо, чи передається створена нами нотатка в HTML-контекст
        self.assertIn(self.note, response.context['notes'])
