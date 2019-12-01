from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Funcionario
from .forms import ClienteForm, FuncionarioForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

def home(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()
    contexto = {
        'clientes': clientes,
        'funcionarios': funcionarios,      
    }
    resposta = render(request, template_name="clientes/home.html", context=contexto)
    return HttpResponse(resposta)

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy('home')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy('home')

def detalhes_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    contexto = {
        'cliente': cliente,    
    }
    resposta = render(request, template_name="clientes/cliente.html", context=contexto)
    return HttpResponse(resposta)
    
def deleta_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('home') 

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/funcionario_form.html"
    success_url = reverse_lazy('home')

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/funcionario_form.html"
    success_url = reverse_lazy('home')

def detalhes_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    contexto = {
        'funcionario': funcionario,    
    }
    resposta = render(request, template_name="funcionarios/funcionario.html", context=contexto)
    return HttpResponse(resposta)

def deleta_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('home')  
