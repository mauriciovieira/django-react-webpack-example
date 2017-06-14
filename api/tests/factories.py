import factory

from .. import models


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    author = factory.Faker('name')
    title = factory.Faker('sentence', nb_words=4)
