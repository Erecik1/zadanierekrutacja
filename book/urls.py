from django.urls import path
from book.views import book_list, add_book

urlpatterns = [
    path('', book_list, name="index"),
    path('add/', add_book),
]
