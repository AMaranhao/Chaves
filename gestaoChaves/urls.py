from django.contrib import admin
from django.urls import path
from .views import chave_list, chave_delete, chave_new, chave_update


urlpatterns = [
    path('list/', chave_list, name="chave_list"),
    path('new/', chave_new, name="chave_new"),
    path('update/<int:id>', chave_update, name="chave_update"),
    path('delete/<int:id>', chave_delete, name="chave_delete"),

]