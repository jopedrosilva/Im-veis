from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('cliente/', views.listaClientes, name='Lista-Clientes'),
    path('cliente/<int:id>', views.clienteView, name='cliente-view'),
    path('newcliente/', views.newCliente, name='new-cliente'),
    path('edit/<int:id>', views.editCliente, name='edit-cliente'),
    path('delete/<int:id>', views.deleteCliente, name='delete-cliente'),
    path('yourname/<str:name>', views.yourName, name='yourname'),

    path('', views.listaVendas, name='Lista-Vendas'),
    path('newvenda/', views.newVenda, name='new-venda'),
    path('venda/<int:id>', views.vendaView, name='venda-view'),
]
