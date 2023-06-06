from django.forms import ModelForm
from BancoDeDados.models import CURSOSENAC
from django.contrib.auth.models import User


class CursoForm(ModelForm):
    class Meta:
        model = CURSOSENAC
        fields = ['Nome', 'Codigo', 'Predio_FK']
        labels = {
            'Predio_FK': 'Predio',
        }

