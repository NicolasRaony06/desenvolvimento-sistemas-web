from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('register_book/', views.register_book, name='register_book'),
    path('view_books/', views.view_books, name="view_books"),
]
