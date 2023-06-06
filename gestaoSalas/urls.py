from django.contrib import admin
from django.urls import path
from .views import sala_list, sala_delete, sala_new, sala_update


urlpatterns = [
    path('list/', sala_list, name="sala_list"),
    path('new/', sala_new, name="sala_new"),
    path('update/<int:id>', sala_update, name="sala_update"),
    path('delete/<int:id>', sala_delete, name="sala_delete"),

]