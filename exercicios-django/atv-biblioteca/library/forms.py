from .models import Book
from django import forms

class LivroForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do livro'}), 
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do autor'}), 'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de publicação'}), 
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Disponível'})
            }