from django.urls import path
from . import views

urlpatterns = [
    path('', views.portifolio, name='portifolio')
]
