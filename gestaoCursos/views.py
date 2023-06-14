from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import CURSOSENAC, FUNCIONARIO
from .forms import CursoForm
from django.db import transaction



@login_required()
def curso_list(request):
    cursos = CURSOSENAC.objects.all()
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)
    autorizaçãoCriarCurso = False
    if (usuarioLogado.Cargo_FK.Nome == 'Coordenador') and (usuarioLogado.Curso_FK.Nome == 'ADS'):
        autorizaçãoCriarCurso = True
    autorizaçãoAtualizarCurso = False
    if (usuarioLogado.Cargo_FK.Nome == 'Coordenador') and (usuarioLogado.Curso_FK.Nome == 'ADS'):
        autorizaçãoAtualizarCurso = True
    context = {
        'cursos':cursos,
        'autorizaçãoCriarCurso':autorizaçãoCriarCurso,
        'autorizaçãoAtualizarCurso': autorizaçãoAtualizarCurso,
    }
    return render(request, 'curso.html', context)


@login_required()
def curso_new(request):
    form = CursoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request, 'cursoForm.html', {'form': form})


@login_required()
def curso_update(request, id):
    curso = get_object_or_404(CURSOSENAC, pk=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)

    if form.is_valid():
        form.save()
        return redirect('curso_list')

    return render(request, 'cursoForm.html', {'form': form})

@login_required()
def curso_delete(request, id):
    curso = get_object_or_404(CURSOSENAC, pk=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)

    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')

    return render(request, 'cursoDeleteConfirm.html', {'form': form})


