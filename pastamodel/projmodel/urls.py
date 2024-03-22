# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', listar_clientes, name='lista_clientes'),
    path('produtos/cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('produtos/', listar_produtos, name='lista_produtos'),
]
