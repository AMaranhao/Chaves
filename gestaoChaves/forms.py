from django.forms import ModelForm
from BancoDeDados.models import CHAVES, FUNCIONARIO


class ChaveForm(ModelForm):
    class Meta:
        model = CHAVES
        fields = ['Numero', 'Numeracao_Armario', 'Salas_FK']
        labels = {
            'Numeracao_Armario': 'Armário',
            'Salas_FK': 'Sala',
        }

    def __init__(self, *args, **kwargs):
        usuario_logado = kwargs.pop('usuario_logado', None)
        super(ChaveForm, self).__init__(*args, **kwargs)

        if self.instance and usuario_logado.Cargo_FK.Nome == 'Recepcionista':
            for field_name in self.fields:
                self.fields[field_name].disabled = True

