from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BancoDeDados.models import CURSOSENAC
from .forms import CursoForm
from django.db import transaction



@login_required()
def curso_list(request):
    cursos = CURSOSENAC.objects.all()
    return render(request, 'curso.html', {'cursos': cursos})


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


