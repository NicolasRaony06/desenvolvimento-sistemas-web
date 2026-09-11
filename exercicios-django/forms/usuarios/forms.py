from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=50)
    email = forms.EmailField(label="Seu email")

    
    

