from django.urls import path
import book.views as book

urlpatterns = [
    path('', book.book_list, name="index"),
    path('add/', book.add_book, name="addbook"),
    path('edit/<int:pk>/', book.edit_book, name="edit"),
    path('import/', book.book_import, name="import"),

    path('api/v1/', book.BookApi.as_view(), name="api"),

]
