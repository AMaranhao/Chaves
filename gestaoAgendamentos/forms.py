from django.forms import ModelForm
from django import forms
from BancoDeDados.models import AGENDAMENTO
from tempus_dominus.widgets import DateTimePicker


#TODO:Fazer com que o agendamento apareca calendario com horarios agendados e horarios frees para sala selecionada
class AgendamentoForm(ModelForm):

    class Meta:
        model = AGENDAMENTO
        fields = ['Funcionario_FK', 'Salas_FK', 'Horario_inicio', 'Horario_fim', 'Kit']
        widgets = {
            'Horario_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'Horario_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'Funcionario_FK': 'Email do Professor',
            'Salas_FK': 'Sala',
        }
