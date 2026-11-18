from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_published_year(value):
    current_year = timezone.now().year
    if not value in range(1450, current_year + 1):
        raise ValidationError(f"O ano de publicação deve estar entre 1450 e {current_year}.")

def validate_pages_number(value):
    if not value in range(1, 5001):
        raise ValidationError(f"O número de páginas do livro deve estar entre 1 a 5000.")

def validate_isbn_lenght(value):
    if not len(str(abs(value))) == 13:
        raise ValidationError(f"Código ISBN deve ter 13 dígitos.")