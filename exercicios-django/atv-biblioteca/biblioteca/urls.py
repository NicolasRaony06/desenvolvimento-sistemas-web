from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('cadastrar_livro/', views.cadastrarLivro, name='cadastrar_livro'),
]
