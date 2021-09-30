from django.urls import path
from book.views import book_list

urlpatterns = [
    path('', book_list),
]
