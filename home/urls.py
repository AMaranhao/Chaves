from django.contrib import admin
from django.urls import path, include
from .views import home, mylogout, menu
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from gestaoFuncionarios import urls as funcionario_urls
from gestaoCursos import urls as curso_urls
from gestaoKits import urls as kit_urls
from gestaoChaves import urls as chave_urls
from gestaoAgendamentos import urls as agendamento_urls
from gestaoSalas import urls as sala_urls
from gestaoEmprestimos import urls as emprestimo_urls



urlpatterns = [
    path('', home, name="home"),
    path('logout/', mylogout, name="logout"),
    path('menu/', menu, name="menu"),
    path('funcionario/', include(funcionario_urls)),
    path('curso/', include(curso_urls)),
    path('kit/', include(kit_urls)),
    path('chave/', include(chave_urls)),
    path('agendamento/', include(agendamento_urls)),
    path('sala/', include(sala_urls)),
    path('emprestimo/', include(emprestimo_urls)),




]