from django.urls import path
from . import views
from estoque.views import index


urlpatterns = [
    path('', index, name='index'),
    path('itens', views.listarItens),
]
