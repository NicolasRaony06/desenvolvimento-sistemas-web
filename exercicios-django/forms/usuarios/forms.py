from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=50,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'})
            )
    email = forms.EmailField(label="Seu email",widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'nome@exemplo.com',
            'autocomplete': 'email'
            })
            )
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@nicolas.corp.com'):
            raise forms.ValidationError("Apenas e-mails da corporação (@nicolas.corp.com) são permitidos")
        return email

    
    

