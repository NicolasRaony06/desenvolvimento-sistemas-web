from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.view_books),
    path('register_book/', views.register_book, name='register_book'),
    path('view_books/', views.view_books, name="view_books"),
    path('view_author_detailed/<int:id>/', views.view_author_detailed, name="view_author_detailed"),
    path('register_author/', views.register_author, name="register_author"),
]
