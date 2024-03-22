from django.contrib import admin
from django.urls import path, include
from appmodelo import views  # Importe as views do aplicativo appmodelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),  # Adicione a view para a página inicial
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
]
