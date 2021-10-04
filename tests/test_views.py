from django.test import TestCase
from django.urls import reverse
from book.models import Book


class ViewTestCase(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(title="TestTitle",
                                         author="TestAuthor",
                                         date_of_publication="2020-10-10",
                                         ISBN_number="TestISBN",
                                         number_of_pages="5",
                                         link_to_cover="https://www.testlink.com",
                                         language="TestLanguage")

    def test_book_list(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_book(self):
        response = self.client.post(reverse('addbook'), data={
            'title': 'TestTitle2',
            "author": "TestAuthor",
            "date_of_publication": "2020-10-10",
            "ISBN_number": "102121",
            "number_of_pages": 1,
            "link_to_cover": "https://www.testlink.com",
            "language": "testLanguage",
        })

        self.assertEqual(response.status_code, 302)
        book = Book.objects.get(id=2)
        self.assertEqual(book.title, "TestTitle2")

    def test_edit_book(self):
        url = reverse('edit', args=['1'])
        response = self.client.post(url, {
                "title": "TestTitleEdited",
                "author": "TestAuthor",
                "date_of_publication": "2020-10-10",
                "ISBN_number": "10111",
                "number_of_pages": 1121,
                "link_to_cover": "https://www.testlink.com",
                "language": "testLanguage",
            })
        self.assertEqual(response.status_code, 302)
        book = Book.objects.get(id=self.book1.id)
        self.assertEqual(book.title, "TestTitleEdited")
