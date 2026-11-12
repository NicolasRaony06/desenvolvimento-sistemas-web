from .models import Book, Author
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_year', 'available', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do livro'}), 
            'authors': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Nome do autor'}),   
            'published_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de publicação'}), 
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Disponível'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'})
            }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'nationality']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Autor'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidade do Autor'})
        }