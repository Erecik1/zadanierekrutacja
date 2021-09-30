from django.db import models


class Book(models.Model):
    tytul = models.CharField(max_length=32)
    autor = models.CharField(max_length=64)
    data_publikacji = models.DateField()
    numer_ISBN = models.CharField(max_length=17)
    liczba_stron = models.IntegerField()
    link_do_okladki = models.URLField(max_length=200)
    jezyk_publikacji = models.CharField(max_length=32)

    def __str__(self):
        return self.tytul
