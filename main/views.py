from django.shortcuts import render
from main.models import *

def index(request):
    return render(request,"index.html")

def produtos(request):
    return render(request, "produtos.html")

def carrinho(request):
    return render(request, "carrinho.html")

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')
