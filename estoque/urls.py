from django.urls import path
from . import views
from estoque.views import index


urlpatterns = [
    path('', index, name='index'),
    path('itens', views.listarItens),

    # Itens
    path('saidaitem/<int:id>', views.saidaItem),
    path('entradaitem/<int:id>', views.entradaItem),
    path('novoEstoque', views.novoEstoque),
    path('editarEstoque/<int:id>', views.editarEstoque),
    path('excluirEstoque/<int:id>', views.excluirEstoque),
    path('gerenciar-itens', views.listarCadastrarItem, name='gerenciar_itens'),
    path('excluirItem/<int:id>', views.excluirItem, name='excluir_item'),
]
