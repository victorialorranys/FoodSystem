from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField()
    valor = models.DecimalField('Preço do produto',max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/',blank=True, null=True, max_length=250)

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    valor = models.DecimalField('Preço do produto',max_digits=8, decimal_places=2)
    quantidade = models.CharField(max_length=20)
    mesa = models.CharField(max_length=5)
    observacao = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete= models.CASCADE)
    
    
class Conta(models.Model):
    pagamento = models.CharField(max_length=80)
    mesa = models.CharField(max_length=5)
    garcom = models.DecimalField('Acréscimo do garçom',max_digits=8, decimal_places=2)
    total = models.DecimalField('Valor total',max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)






