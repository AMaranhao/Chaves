from django.forms import ModelForm
from BancoDeDados.models import SALAS


class SalaForm(ModelForm):
    class Meta:
        model = SALAS
        fields = ['Numero', 'Tipo_de_Kit', 'Tipo_Sala_FK', 'Ocupada']
        labels = {
            'Tipo_de_Kit': 'Tipo de Kit',
            'Tipo_Sala_FK': 'Tipo de Sala',
        }
