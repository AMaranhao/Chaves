from django.forms import ModelForm
from BancoDeDados.models import CHAVES


class ChaveForm(ModelForm):
    class Meta:
        model = CHAVES
        fields = ['Numero', 'Numeracao_Armario', 'Salas_FK']
        labels = {
            'Numeracao_Armario': 'Armário',
            'Salas_FK': 'Sala',
        }
