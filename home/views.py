from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from BancoDeDados.models import FUNCIONARIO


def home(request):
    return render(request, 'home.html')


@login_required
def menu(request):
    usuarioLogado = FUNCIONARIO.objects.get(User_FK=request.user)
    context = {
        'usuarioLogado':usuarioLogado,
    }
    return render(request, 'menu.html', context)


@login_required
def mylogout(request):
    logout(request)
    return render('home.html')