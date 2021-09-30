from django.shortcuts import render, redirect
from book.models import Book
from book.forms import BookForm
from django.db.models import Q


def is_valid_queryparam(param):
    return param != '' and param is not None


def book_list(request):
    book_filter = Q()
    title = request.GET.get('title')
    author = request.GET.get('author')
    language = request.GET.get('language')
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    if is_valid_queryparam(title):
        book_filter &= Q(title__icontains=title)
    if is_valid_queryparam(author):
        book_filter &= Q(author__icontains=author)
    if is_valid_queryparam(language):
        book_filter &= Q(language=language)
    if is_valid_queryparam(start_date):
        book_filter &= Q(date_of_publication__gte=start_date)
    if is_valid_queryparam(end_date):
        book_filter &= Q(date_of_publication__lte=end_date)
    if is_valid_queryparam(book_filter):
        books = Book.objects.filter(book_filter, )
    else:
        books = Book.objects.all()
    return render(request, 'index.html',
                  {'books': books})


def add_book(request):
    form = BookForm()
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(book_list)
    return render(request, 'add_book.html', {'form': form})
