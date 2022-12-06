from django.contrib import admin
from main.models import *


class ProdutoAdmin(admin.ModelAdmin):
    list_display= ('id', 'nome')

admin.site.register(Categoria)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente)
admin.site.register(Pedido)


