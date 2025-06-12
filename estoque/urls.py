from django.urls import path
from . import views
from estoque.views import EstoqueViewSet, index
from rest_framework.routers import DefaultRouter
from .models import Estoque


router = DefaultRouter(
    trailing_slash=False
)

router.register(r'estoque', EstoqueViewSet)

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

urlpatterns += router.urls