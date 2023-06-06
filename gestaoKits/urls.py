from django.contrib import admin
from django.urls import path
from .views import kit_list, kit_delete, kit_new, kit_update


urlpatterns = [
    path('list/', kit_list, name="kit_list"),
    path('new/', kit_new, name="kit_new"),
    path('update/<int:id>', kit_update, name="kit_update"),
    path('delete/<int:id>', kit_delete, name="kit_delete"),

]