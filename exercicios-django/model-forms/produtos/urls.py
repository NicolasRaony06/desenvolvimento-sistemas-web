from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name="cadastrar_produto"),
    path('produtos/', views.produtos, name='produtos')
]