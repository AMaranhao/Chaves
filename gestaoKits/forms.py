from django.forms import ModelForm
from BancoDeDados.models import KITS


class KitForm(ModelForm):
    class Meta:
        model = KITS
        fields = ['Numero', 'Numeracao_Armario', 'Tipo_de_Kit']
        labels = {
            'Numeracao_Armario': 'Armario',
        }
