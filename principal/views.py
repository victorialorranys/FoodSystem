from django.shortcuts import render
from principal.models import *

def index(request):
    return render(request,"index.html")

def produtos(request):
    lista = Produto.objects.all()
    context = {'produtos': lista}
    return render (request, 'produtos.html',context)

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def detalhes (request,id):
    produto = Produto.objects.get(id=id)
    context = {'produto': produto}
    return render (request, 'detalhes.html', context)
