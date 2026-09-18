from django.shortcuts import render, redirect
from .forms import LivroForm

# Create your views here.
def cadastrarLivro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('biblioteca:cadastrar_livro')
    else:
        form = LivroForm()
    return render(request, 'livro/cadastrar.html', {'form': form})