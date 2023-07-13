from django.forms import ModelForm
from BancoDeDados.models import EMPRESTIMOS

class EmprestimoForm(ModelForm):
    class Meta:
        model = EMPRESTIMOS
        fields = ['Funcionario_FK', 'Chaves_FK', 'Horario_Recepcao', 'Horario_Devolucao', 'Kit_FK']
        labels = {
                'Funcionario_FK': 'Professor',
                'Chaves_FK': 'Chaves',
                'Horario_Recepcao': 'Horario Recepção',
                'Horario_Devolucao': 'Horario Devolucao',
                'Kit_FK': 'Kit',
        }


