from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import BookForm, AuthorForm
from .models import Book, Author

# Create your views here.
# def register_book(request, id=None):
#     book = None
#     if id:
#         book = get_object_or_404(
#             Book,
#             id=id
#         )

#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             form.save()
#             authors_id = ','.join(str(author.id) for author in form.cleaned_data['authors'])
#             return redirect('library:view_author_detailed', authors_id)
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'book/register_edit.html', {'form': form})

class BookFormValidMixin:
    def form_valid(self, form):
        form.save()
        author_id = form.cleaned_data['authors'].first()
        return redirect('library:view_author_detailed', author_id.id)

class BookRegisterView(BookFormValidMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/register_edit.html'

class BookEditView(BookFormValidMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/register_edit.html'

# def view_books(request):
#     books = Book.objects.prefetch_related('authors')
#     return render(request, 'book/view.html', {'books': books})

class BooksView(ListView):
    model = Book
    template_name = 'book/view.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.order_by("title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_available'] = Book.objects.filter(available=True).count()
        return context

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book/delete.html"
    success_url = reverse_lazy("library:view_books")

# def view_author_detailed(request, id):   
#     try:
#         authors_id = list(map(int, id.split(',')))
#     except Exception as error:
#         return HttpResponseBadRequest(f"Informe corretamente a os ID's para autores, ex: ids=1,2,3. {str(error)}")

#     authors = get_list_or_404(
#         Author.objects.prefetch_related('books'),
#         id__in=authors_id
#     )

#     return render(request, 'author/view_detailed.html', {'authors': authors})

class AuthorDetailedView(DetailView):
    model = Author
    template_name = "author/view_detailed.html"

# def register_author(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             author = form.save()
#             return redirect('library:view_author_detailed', author.id)
#     else:
#         form = AuthorForm()
#     return render(request, 'author/register.html', {'form': form})

class AuthorRegisterView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "author/register.html"

    def form_valid(self, form):
        self.object = form.save()
        return redirect('library:view_author_detailed', self.object.id)

