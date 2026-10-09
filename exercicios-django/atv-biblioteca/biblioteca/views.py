from django.shortcuts import render, redirect
from .forms import LivroForm
from .models import Book

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
        books = Book.objects.all()
        return render(request, 'book/view.html', {'books': books})