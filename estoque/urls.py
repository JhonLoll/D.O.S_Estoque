from django.urls import path
from . import views
from estoque.views import EstoqueViewSet, index
from rest_framework.routers import DefaultRouter
# from .models import Estoque


router = DefaultRouter(
    trailing_slash=False
)

router.register(r'estoque', EstoqueViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('itens', views.listarItens, name='listar_itens'),

    # Itens
    # path('saidaitem/<int:id>', views.saidaItem),
    # path('entradaitem/<int:id>', views.entradaItem),
    path('novoEstoque', views.novoEstoque, name='novo_estoque'),
    path('editarEstoque/<int:id>', views.editarEstoque, name='editar_estoque'),
    path('excluirEstoque/<int:id>', views.excluirEstoque, name='excluir_estoque'),
    path('gerenciar-itens', views.listarCadastrarItem, name='gerenciar_itens'),
    path('excluirItem/<str:item_id>/', views.excluirItem, name='excluir_item'), # Alterado de <int:id> para <str:item_id>
]

urlpatterns += router.urls