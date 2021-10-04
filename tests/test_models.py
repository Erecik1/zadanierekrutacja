from django.test import TestCase
from book.models import Book

class ModelTestCase(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(title="TestTitle",
                                         author="TestAuthor",
                                         date_of_publication="2020-10-10",
                                         ISBN_number="TestISBN",
                                         number_of_pages="5",
                                         link_to_cover="https://www.testlink.com",
                                         language="TestLanguage")

    def test_title(self):
        self.assertEqual(self.book1.title, "TestTitle")