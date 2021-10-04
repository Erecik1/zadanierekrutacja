from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=64, null=True)
    date_of_publication = models.DateField(null=True)
    ISBN_number = models.CharField(max_length=17, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    link_to_cover = models.URLField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.title
