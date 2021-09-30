from django.shortcuts import render
from book.models import Book
from book.forms import BookForm


def book_list(request):
    books = Book.objects.all()
    form = BookForm()
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Book.objects.filter()
            return render(request, 'index.html', {"results": results})

    return render(request, 'index.html',
                  {'books': books, 'form': form})

def add_book(request):
    form = BookForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
