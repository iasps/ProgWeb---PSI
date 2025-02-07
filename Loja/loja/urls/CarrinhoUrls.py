from django.urls import path
from loja.views.CarrinhoView import create_carrinhoitem_view
from loja.views.CarrinhoView import list_carrinho_view
from loja.views.CarrinhoView import confirmar_carrinho_view
from loja.views.CarrinhoView import remover_item_view
from loja.views.CarrinhoView import atualizar_quantidade

urlpatterns = [
    path("", list_carrinho_view, name='list_carrinho'),
    path("<int:produto_id>", create_carrinhoitem_view, name='create_carrinhoitem'),
    path("confirmar", confirmar_carrinho_view, name='confirmar_carrinho'),
    path('remover/<int:item_id>/', remover_item_view, name='remover_carrinhoitem'),
    path('atualizar_quantidade/<int:item_id>/', atualizar_quantidade, name='atualizar_quantidade'),
]