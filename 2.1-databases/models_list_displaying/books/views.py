from django.shortcuts import render
from books.models import Book
from django.urls import reverse
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def book_view(request):
    template = 'books/book.html'
    books = {'name': Book.objects.values().filter(pub_date='2018-02-27')[0].get('name')}

    paginator = Paginator(books, 5)
    page_number = int(request.GET.get('page'), 1)
    page = paginator.get_page(page_number)
    context = {'book': page}
    return render(request, template, context)