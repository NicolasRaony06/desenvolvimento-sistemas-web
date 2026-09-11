from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao']
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),'preco': forms.NumberInput(attrs={'class': 'form-control'}), 'descricao': forms.Textarea(attrs={'class': 'form-control'})}