from django.urls import path
from .views import (
    ProdutoListView, ProdutoCreateView,
    ProdutoUpdateView, ProdutoDeleteView
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('deletar/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),
]
