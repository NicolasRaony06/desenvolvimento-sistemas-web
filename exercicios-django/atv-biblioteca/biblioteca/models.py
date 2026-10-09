from django.db import models

# Create your models here.
class Book(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.PROTECT, related_name="books")
    published_year = models.IntegerField()
    available = models.BooleanField(default=True)
    categories = models.ManyToManyField("Category", related_name="books")

    class Meta:
        ordering = ['tittle']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'    

    def __str__(self):
        return self.tittle    

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

    def __str__(self):
        return self.name

    