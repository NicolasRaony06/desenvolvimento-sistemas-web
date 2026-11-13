from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'library'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='library:view_books')),
    path('register_book/', views.register_book, name='register_book'),
    path('edit_book/<int:id>/', views.register_book, name='edit_book'),
    path('view_books/', views.view_books, name="view_books"),
    path('view_author_detailed/<int:id>/', views.view_author_detailed, name="view_author_detailed"),
    path('register_author/', views.register_author, name="register_author"),
]
