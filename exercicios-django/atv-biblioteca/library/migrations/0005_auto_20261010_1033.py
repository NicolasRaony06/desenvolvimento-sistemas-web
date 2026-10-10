from django.db import migrations

def copiar_autores_para_many_to_many(apps, schema_editor):
    Book = apps.get_model('library', 'Book')
    
    for book in Book.objects.all():
        if book.author: # Se o livro tiver um autor antigo vinculado
            book.authors.add(book.author) # Adiciona na nova relação ManyToMany

def reverter_copia(apps, schema_editor):
    Book = apps.get_model('library', 'Book')
    
    for book in Book.objects.all():
        book.authors.clear() # Limpa a relação ManyToMany se desfeita

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_authors_alter_book_author'), # Nome da migração anterior automática
    ]

    operations = [
        migrations.RunPython(copiar_autores_para_many_to_many, reverse_code=reverter_copia),
    ]
