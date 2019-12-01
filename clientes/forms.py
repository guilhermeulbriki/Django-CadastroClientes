from django import forms
from .models import Cliente, Funcionario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'endereco', 'telefone', 'cpf')

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'apelido', 'snap', 'cpf')