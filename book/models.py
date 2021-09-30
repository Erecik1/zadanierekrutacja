from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=64)
    date_of_publication = models.DateField()
    ISBN_number = models.CharField(max_length=17)
    number_of_pages = models.IntegerField()
    link_to_cover = models.URLField(max_length=200)
    language = models.CharField(max_length=32)

    def __str__(self):
        return self.title
