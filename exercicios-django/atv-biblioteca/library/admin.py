from django.contrib import admin
from .models import Book, Author, Category

# Register your models here.
class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'author', 'published_year', 'available']
    list_filter = ['available', 'categories']
    filter_horizontal = ['categories']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...