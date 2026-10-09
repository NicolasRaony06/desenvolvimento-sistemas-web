from django.shortcuts import render, redirect, get_object_or_404
from .forms import LivroForm
from .models import Book, Author

# Create your views here.
def register_book(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('library:register_book')
    else:
        form = LivroForm()
    return render(request, 'book/register.html', {'form': form})

def view_books(request):
    if request.method == 'GET':
        books = Book.objects.select_related('author')
        return render(request, 'book/view.html', {'books': books})

def view_author_detailed(request, id):
    author = get_object_or_404(
        Author.objects.prefetch_related('books'),
        id=id
    )

    return render(request, 'author/view_detailed.html', {'author': author})