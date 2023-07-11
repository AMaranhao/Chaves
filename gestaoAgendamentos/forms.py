from django.forms import ModelForm
from django import forms
from BancoDeDados.models import AGENDAMENTO, FUNCIONARIO
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

        def __init__(self, *args, **kwargs):
            super(AgendamentoForm, self).__init__(*args, **kwargs)

            current_user = kwargs['initial']['request'].user
            funcionarios = FUNCIONARIO.objects.filter(Curso_FK=current_user.funcionario.Curso_FK).order_by('first_name')

            self.fields['Funcionario_FK'].queryset = funcionarios
'''
            funcionario_logado = FUNCIONARIO.objects.get(User_FK=kwargs['initial']['request'].user)

            if funcionario_logado.Cargo_FK.Nome != 'Coordenador' and funcionario_logado.Cargo_FK.Nome != 'Recepcionista':
                for field_name in self.fields:
                    if field_name != 'Kit':  # Exclua o campo 'Kit' da lista de campos desabilitados
                        self.fields[field_name].disabled = True

'''