from django.contrib import admin
from django.urls import path
from .views import emprestimo_list, emprestimo_delete, emprestimo_new, emprestimo_update


urlpatterns = [
    path('list/', emprestimo_list, name="emprestimo_list"),
    path('new/', emprestimo_new, name="emprestimo_new"),
    path('update/<int:id>', emprestimo_update, name="emprestimo_update"),
    path('delete/<int:id>', emprestimo_delete, name="emprestimo_delete"),

]