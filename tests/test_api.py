from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from book.models import Book


class QuerystringsApiTestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(title="TestTitle",
                                        author="TestAuthor",
                                        date_of_publication="2020-10-10",
                                        ISBN_number="TestISBN",
                                        number_of_pages="5",
                                        link_to_cover="https://www.testlink.com",
                                        language="TestLanguage")

    api_url = reverse("api")

    def set_query(self, key, value):
        return f"{key}={value}"

    def test_title(self):
        response = self.client.get(self.api_url + "?" + self.set_query("title", "TestTitle"))
        self.assertEqual(response.json()[0]["title"], "TestTitle")

    def test_author(self):
        response = self.client.get(self.api_url + "?" + self.set_query("author", "TestAuthor"))
        self.assertEqual(response.json()[0]["author"], "TestAuthor")

    def test_date_of_publication(self):
        response = self.client.get(self.api_url + "?" + self.set_query("date_of_publication", "2020-10-10"))
        self.assertEqual(response.json()[0]["date_of_publication"], "2020-10-10")

    def test_ISBN_number(self):
        response = self.client.get(self.api_url + "?" + self.set_query("ISBN_number", "TestISBN"))
        self.assertEqual(response.json()[0]["ISBN_number"], "TestISBN")

    def test_number_of_pages(self):
        response = self.client.get(self.api_url + "?" + self.set_query("number_of_pages", "5"))
        self.assertEqual(response.json()[0]["number_of_pages"], 5)

    def test_link_to_cover(self):
        response = self.client.get(self.api_url + "?" + self.set_query("link_to_cover", "https://www.testlink.com"))
        self.assertEqual(response.json()[0]["link_to_cover"], "https://www.testlink.com")

    def test_language(self):
        response = self.client.get(self.api_url + "?" + self.set_query("language", "TestLanguage"))
        self.assertEqual(response.json()[0]["language"], "TestLanguage")