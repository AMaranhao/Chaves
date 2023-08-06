from django.contrib import admin
from django.urls import path
from .views import agendamento_list, agendamento_delete, agendamento_new, agendamento_update, agendamento_emprestimo


urlpatterns = [
    path('list/', agendamento_list, name="agendamento_list"),
    path('new/', agendamento_new, name="agendamento_new"),
    path('update/<int:id>', agendamento_update, name="agendamento_update"),
    path('delete/<int:id>', agendamento_delete, name="agendamento_delete"),
    path('agendamentoEmprestimo', agendamento_emprestimo, name="agendamento_emprestimo"),

]