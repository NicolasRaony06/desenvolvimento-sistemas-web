from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseBadRequest
from .forms import BookForm, AuthorForm
from .models import Book, Author

# Create your views here.
def register_book(request, id=None):
    book = None
    if id:
        book = get_object_or_404(
            Book,
            id=id
        )

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            authors_id = ','.join(str(author.id) for author in form.cleaned_data['authors'])
            return redirect('library:view_author_detailed', authors_id)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/register_edit.html', {'form': form})

def view_books(request):
    books = Book.objects.prefetch_related('authors')
    return render(request, 'book/view.html', {'books': books})

def view_author_detailed(request, id):   
    try:
        authors_id = list(map(int, id.split(',')))
    except Exception as error:
        return HttpResponseBadRequest(f"Informe corretamente a os ID's para autores, ex: ids=1,2,3. {str(error)}")

    authors = get_list_or_404(
        Author.objects.prefetch_related('books'),
        id__in=authors_id
    )

    return render(request, 'author/view_detailed.html', {'authors': authors})

def register_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('library:view_author_detailed', author.id)
    else:
        form = AuthorForm()
    return render(request, 'author/register.html', {'form': form})