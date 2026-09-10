from django.shortcuts import render, redirect
from .forms import ContatoForm

# Create your views here.
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            print(nome, email)

            return redirect('contato')
    else:
        form = ContatoForm()
        
    return render(request, 'usuarios/contato.html', {"form": form})