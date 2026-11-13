from .models import Book, Author
from django import forms
from datetime import date

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

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 3:
            raise forms.ValidationError('Título não pode ter menos que 3 caracteres')
        return title

    def clean_published_year(self):
        published_year = self.cleaned_data['published_year']

        if published_year > date.today().year:
            raise forms.ValidationError("Ano de publicação não pode posterior ao ano atual.")
        return published_year


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'nationality']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Autor'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidade do Autor'})
        }