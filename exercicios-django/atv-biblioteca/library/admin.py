from django.contrib import admin
from .models import Book, Author, Category

# Register your models here.
class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_authors', 'published_year', 'available']
    list_filter = ['available', 'categories']
    filter_horizontal = ['categories']

    @admin.display(description="Autores")
    def get_authors(self, obj):
        return ', '.join([author.name for author in obj.authors.all()])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...