from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def book_view(request, pub_date):
    template = 'books/book.html'
    try:
        pub_dates_prev = Book.objects.values().filter(pub_date__lt=pub_date)[0].get('pub_date')
        pub_dates_next = Book.objects.values().filter(pub_date__gt=pub_date)[0].get('pub_date')
    except IndexError:
        pub_dates_next = Book.objects.values().first().get('pub_date')
        pub_dates_prev = Book.objects.values().last().get('pub_date')

    context = {'books': Book.objects.filter(pub_date=pub_date),
               'pub_dates_prev': pub_dates_prev,
               'pub_dates_next': pub_dates_next,
               }
    print(context)
    return render(request, template, context)
