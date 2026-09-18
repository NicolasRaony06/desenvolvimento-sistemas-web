from .models import Livro
from django import forms

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do livro'}), 
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do autor'}), 'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de publicação'}), 
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Disponível'})
            }