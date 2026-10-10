from django.contrib import admin
from .models import Book, Author, Category

# Register your models here.
class BookInline(admin.TabularInline):
    model = Author.books.through

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'get_authors', 'published_year', 'available']
    list_filter = ['available', 'categories']
    filter_horizontal = ['categories']

    def get_authors(self, obj):
        # Junta o nome de todos os autores separados por vírgula
        return ", ".join([author.name for author in obj.authors.all()])
    
    get_authors.short_description = 'Autores'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...