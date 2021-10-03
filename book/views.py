from datetime import datetime

import requests
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from book.forms import BookForm, BookImportForm
from book.models import Book
from book.serializers import BookSerializers


def is_valid_queryparam(param):
    return param != '' and param is not None


def define_filtrs(request):
    book_filter = Q()
    title = request.GET.get('title')
    author = request.GET.get('author')
    language = request.GET.get('language')
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    if is_valid_queryparam(title):
        book_filter &= Q(title=title)
    if is_valid_queryparam(author):
        book_filter &= Q(author__icontains=author)
    if is_valid_queryparam(language):
        book_filter &= Q(language=language)
    if is_valid_queryparam(start_date):
        book_filter &= Q(date_of_publication__gte=start_date)
    if is_valid_queryparam(end_date):
        book_filter &= Q(date_of_publication__lte=end_date)
    if is_valid_queryparam(book_filter):
        return Book.objects.filter(book_filter, )
    else:
        return Book.objects.all()


def book_list(request):
    books = define_filtrs(request)
    return render(request, 'index.html',
                  {'books': books})


def add_book(request):
    form = BookForm()
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, 'add_book.html',
                  context={"form": form})


def edit_book(request, pk):
    book = get_object_or_404(Book,
                             pk=pk)
    form = BookForm(instance=book)
    if request.POST:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "edit_book.html",
                  context={"form": form})


def book_import(request):
    form = BookImportForm
    saved_to_database = []
    api_google_url = "https://www.googleapis.com/books/v1/volumes?q="
    if request.POST:
        querystrings = ""
        for key, value in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue
            if value != "":
                querystrings += f"+{key}:{value}"
        r = requests.get(api_google_url + querystrings)
        books_json = r.json()
        for item in books_json["items"]:
            title = item['volumeInfo']['title']
            try:
                author = item['volumeInfo']['authors']
            except KeyError:
                author = None
            try:
                date_of_publication = item['volumeInfo']['publishedDate']
                date_of_publication = date_of_publication.replace("-", "/")
                if len(date_of_publication) == 4:
                    date_of_publication += "/01"
                if len(date_of_publication) == 7:
                    date_of_publication += "/01"
                date_of_publication = datetime.strptime(date_of_publication, '%Y/%m/%d')
            except KeyError:
                date_of_publication = None
            try:
                ISBN_number = item['volumeInfo']['industryIdentifiers'][0]['identifier']
            except KeyError:
                ISBN_number = None
            for industryIdentifiers in item['volumeInfo']['industryIdentifiers']:
                if industryIdentifiers["type"] == "ISBN_13":
                    ISBN_number = industryIdentifiers['identifier']
            try:
                number_of_pages = item['volumeInfo']['pageCount']
            except KeyError:
                number_of_pages = None
            try:
                link_to_cover = item['volumeInfo']['imageLinks']['thumbnail']
            except KeyError:
                link_to_cover = None
            try:
                language = item['volumeInfo']['language']
            except KeyError:
                language = None
            book = Book(title=title, author=author, date_of_publication=date_of_publication,
                        ISBN_number=ISBN_number, number_of_pages=number_of_pages,
                        link_to_cover=link_to_cover, language=language)
            book.save()
            saved_to_database.append(title)
        return render(request, 'import_book.html',
                      context={"form": form, "saved_to_database": saved_to_database})
    return render(request, "import_book.html",
                  context={"form": form})


class BookApi(APIView):
    def get(self, request):
        books = define_filtrs(request)
        serializers = BookSerializers(books, many=True, context={"request": request})
        return Response(serializers.data)
