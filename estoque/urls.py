from django.urls import path
from . import views
from estoque.views import index


urlpatterns = [
    path('', index, name='index'),
    path('itens', views.listarItens),
    path('saidaItem/<int:id>', views.saidaItem),
    path('entradaItem/<int:id>', views.entradaItem),
    path('novoEstoque', views.novoEstoque),
    path('editarEstoque/<int:id>', views.editarEstoque),
    path('excluirEstoque/<int:id>', views.excluirEstoque),
]
