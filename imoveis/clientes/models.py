from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

STATUS = (
    ('À Vista', 'À Vista'),
    ('180 Parcelas', '180 Parcelas')
)

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    numero = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    imovel = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    idCorretor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    pagamento = models.CharField(max_length=255, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imovel
