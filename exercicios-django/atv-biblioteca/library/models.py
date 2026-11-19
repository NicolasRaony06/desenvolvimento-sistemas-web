from django.db import models
from django.core.validators import MinLengthValidator, FileExtensionValidator
from .validators import *

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=200, 
        validators=[
            MinLengthValidator(3, message="Título deve ter no mínimo 3 caracteres")
        ])
    authors = models.ManyToManyField("Author", related_name="books")
    published_year = models.IntegerField(validators=[validate_published_year])
    pages = models.IntegerField(null=True, blank=True, validators=[validate_pages_number])
    isbn = models.IntegerField(
        null=True, 
        blank=True, 
        validators=[
            validate_isbn_lenght
        ])
    cover = models.ImageField(
        upload_to="books/", 
        null=True, 
        blank=True,
        validators=[
            FileExtensionValidator(
                ['jpg', 'jpeg', 'png'], 
                message="O formato do arquivo deve ser jpg, jpeg ou png"
            ),
            validate_file_size
        ]
    )
    available = models.BooleanField(default=True)
    categories = models.ManyToManyField("Category", related_name="books", blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'    

    def __str__(self):
        return self.title    

class Author(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'        

    def __str__(self):
        return self.name

    