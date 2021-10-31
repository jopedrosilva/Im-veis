from django import forms
from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ClienteForm, VendaForm
from django.contrib import messages

from .models import Cliente, Venda

@login_required
def listaClientes(request):
    search = request.GET.get('search')
    if search:
        clientes = Cliente.objects.filter(nome__icontains=search)
    else: 
        clientes_list = Cliente.objects.all().order_by('-created_at')
        paginator = Paginator(clientes_list, 5)
        page = request.GET.get('page')
        clientes = paginator.get_page(page)
    return render(request, 'clientes/lista.html', {'clientes': clientes})

@login_required
def clienteView(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'clientes/cliente.html', {'cliente': cliente})

@login_required
def newCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            messages.info(request, 'Cliente adicionado com sucesso!')
            return redirect('/')
    else:
        form = ClienteForm()
        return render(request, 'clientes/addcliente.html', {'form': form})

@login_required
def editCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if(form.is_valid()):
            cliente.save()
            messages.info(request, 'Cliente editado com sucesso!')
            return redirect('/')
        else:
            return render(request, 'clientes/editcliente.html', {'form': form, 'cliente': cliente})
    else:
        return render(request, 'clientes/editcliente.html', {'form': form, 'cliente': cliente})

@login_required
def deleteCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.info(request, 'Cliente deletado com sucesso!')
    return redirect('/')

def helloworld(request):
    return HttpResponse('Hello World!')

def yourName(request, name):
    return render(request, 'clientes/yourname.html', {'name': name})

@login_required
def listaVendas(request): 
    vendas_list = Venda.objects.all().order_by('-created_at')
    paginator = Paginator(vendas_list, 5)
    page = request.GET.get('page')
    vendas = paginator.get_page(page)
    return render(request, 'vendas/lista.html', {'vendas': vendas})

@login_required
def newVenda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.save()
            messages.info(request, 'Venda adicionada com sucesso!')
            return redirect('/')
    else:
        form = VendaForm()
        return render(request, 'vendas/addvenda.html', {'form': form})

@login_required
def vendaView(request, id):
    venda = get_object_or_404(Venda, pk=id)
    return render(request, 'vendas/venda.html', {'venda': venda})
