from django.db import models

# Create your models here.
class Book(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.PROTECT, related_name="books")
    published_year = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['tittle']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'        


    