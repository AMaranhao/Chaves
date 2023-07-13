from django.forms import ModelForm
from BancoDeDados.models import SALAS
from django import forms


class SalaForm(ModelForm):
    Esta_ativa = forms.NullBooleanField(
        widget=forms.CheckboxInput)
    class Meta:
        model = SALAS
        fields = ['Numero', 'Tipo_de_Kit', 'Tipo_Sala_FK', 'Esta_ativa']
        labels = {
            'Tipo_de_Kit': 'Tipo de Kit',
            'Tipo_Sala_FK': 'Tipo de Sala',
            'Esta_ativa': 'Esta ativa',
        }


