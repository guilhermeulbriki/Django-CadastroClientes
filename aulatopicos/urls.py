from django.contrib import admin
from django.urls import path
from clientes import views as cliente_views

urlpatterns = [
    path('', cliente_views.home, name='home'),
    path('cliente/add/', cliente_views.ClienteCreateView.as_view(), name="add_cliente"),
    path('funcionario/add/', cliente_views.FuncionarioCreateView.as_view(), name="add_funcionario"),
    path('cliente/<int:pk>/', cliente_views.detalhes_cliente, name="detalhes_cliente"),
    path('funcionario/<int:pk>/', cliente_views.detalhes_funcionario, name="detalhes_funcionario"),
    path('cliente/<int:pk>/update/', cliente_views.ClienteUpdateView.as_view(), name="update_cliente"),
    path('cliente/<int:pk>/deleta/', cliente_views.deleta_cliente, name="deleta_cliente"),
    path('funcionario/<int:pk>/update/', cliente_views.FuncionarioUpdateView.as_view(), name="update_funcionario"),
    path('funcionario/<int:pk>/deleta/', cliente_views.deleta_funcionario, name="deleta_funcionario"),
    path('admin/', admin.site.urls),
]
