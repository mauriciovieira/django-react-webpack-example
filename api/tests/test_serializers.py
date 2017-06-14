from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from .factories import BookFactory
from ..serializers import BookSerializer


class BookSerializerTests(APITestCase):

    def test_book_serializer_has_desired_fields(self):
        book = BookFactory()
        book_serializer = BookSerializer(book)

        expected = {
            'author': book.author,
            'title': book.title,
        }
        self.assertEquals(book_serializer.data, expected)
