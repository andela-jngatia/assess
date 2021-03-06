from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from models import Book


def get_books(request):
    """Return list of books, allow for search by name."""
    try:
        q = request.GET['name']
        books = Book.objects.filter(title=q)
    except KeyError:
        try:
            t = int(request.GET['limit'])
            books = Book.objects.all()[:t]
        except KeyError:
            books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


def delete_book(request, pk):
    """Remove book from library."""
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


def read_book(request, pk):
    """Mark book as read or not."""
    book = get_object_or_404(Book, pk=pk)
    book.read = False if book.read else True
    book.save()
    return redirect(get_books)
