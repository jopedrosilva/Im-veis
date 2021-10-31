from django import forms
from django.forms import fields

from .models import Cliente
from .models import Venda

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome', 'cpf', 'email', 'numero')

class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ('imovel', 'rua', 'cidade', 'estado', 'valor', 'idCorretor', 'cliente', 'pagamento')
