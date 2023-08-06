from django.forms import ModelForm
from django import forms
from BancoDeDados.models import EMPRESTIMOS, CURSOSENAC, FUNCIONARIO


class CursoEmprestimoForm(ModelForm):
    class Meta:
        model = FUNCIONARIO
        fields = ['Curso_FK']
        labels = {
                'Curso_FK': 'Curso',
        }
        widgets = {
        'Curso_FK': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CursoEmprestimoForm, self).__init__(*args, **kwargs)
        self.fields['Curso_FK'].queryset = self.fields['Curso_FK'].queryset.exclude(Nome='Administrativo')


class EmprestimoForm(ModelForm):
    class Meta:
        model = EMPRESTIMOS
        fields = ['Funcionario_FK', 'Chaves_FK', 'Kit_FK']
        labels = {
                'Funcionario_FK': 'Professor',
                'Chaves_FK': 'Chaves',
                'Kit_FK': 'Kit'
        }

    def __init__(self, *args, **kwargs):
        curso_fk = kwargs.pop('curso_fk', None)
        super(EmprestimoForm, self).__init__(*args, **kwargs)

        if curso_fk:
            self.fields['Funcionario_FK'].queryset = FUNCIONARIO.objects.filter(Curso_FK__Nome=curso_fk)


