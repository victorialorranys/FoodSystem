from django.shortcuts import render
from principal.models import *
from principal.forms import *

def index(request):
    return render(request,"index.html")

def produtos(request):
    lista = Produto.objects.all()
    context = {'produtos': lista}
    return render (request, 'produtos.html',context)

def cadastro_cliente(request):
    form = ClienteForm()
    return render(request, 'cadastro_cliente.html', {'form' : form })

def carrinho(request):
    return render(request, 'carrinho.html')

def detalhes (request,id):
    produto = Produto.objects.get(id=id)
    context = {'produto': produto}
    return render (request, 'detalhes.html', context)
