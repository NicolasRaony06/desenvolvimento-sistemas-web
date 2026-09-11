from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

# Create your views here.
def produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        return render(request, 'produtos/produtos.html', {'produtos':produtos})

def cadastrar_produto(request):
    print(request)
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar_produto.html', {'form': form})