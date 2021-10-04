from django.urls import reverse
from django.test import TestCase
from book.models import Book

class UrlsTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="TestTitle",
                                        author="TestAuthor",
                                        date_of_publication="2020-10-10",
                                        ISBN_number="TestISBN",
                                        number_of_pages="5",
                                        link_to_cover="https://www.testlink.com",
                                        language="TestLanguage")
    def test_add(self):
        response = self.client.get(reverse('addbook'))
        self.assertEqual(response.status_code, 200)

    def test_edit_not_found(self):
        response = self.client.get(reverse('edit', args=['0']))
        self.assertEqual(response.status_code, 404)

    def test_edit(self):
        response = self.client.get(reverse('edit', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_import(self):
        response = self.client.get(reverse('import'))
        self.assertEqual(response.status_code, 200)
