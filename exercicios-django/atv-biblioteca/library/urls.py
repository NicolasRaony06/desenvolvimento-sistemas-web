from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'library'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='library:view_books')),
    path('register_book/', views.BookRegisterView.as_view(), name='register_book'),
    path('edit_book/<int:pk>/', views.BookEditView.as_view(), name='edit_book'),
    path('view_books/', views.BooksView.as_view(), name="view_books"),
    path('delete_book/<int:pk>/', views.BookDeleteView.as_view(), name="delete_book"),
    path('view_author_detailed/<int:pk>/', views.AuthorDetailedView.as_view(), name="view_author_detailed"),
    path('register_author/', views.AuthorRegisterView.as_view(), name="register_author"),
]
