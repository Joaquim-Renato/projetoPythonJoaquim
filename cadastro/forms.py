from django import forms
from .models import Pacientes


class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome', 'email', 'senha', 'cpf', 'nascimento', 'genero', 'endereco', 'celular', 'contatoEmergencial']