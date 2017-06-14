from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Book


class BookListTests(APITestCase):

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        url = reverse('book-list')
        data = {
            'title': 'Also sprach Zarathustra: Ein Buch für Alle und Keinen',
            'author': 'Friedrich Wilhelm Nietzsche',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().author, 'Friedrich Wilhelm Nietzsche')