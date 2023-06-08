from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import funcionario_list, funcionario_delete, funcionario_update, funcionario_new, change_password_success#, change_password




urlpatterns = [
    path('list/', funcionario_list, name="funcionario_list"),
    path('new/', funcionario_new, name="user_new"),
    path('update/<int:id>', funcionario_update, name="funcionario_update"),
    path('delete/<int:id>', funcionario_delete, name="funcionario_delete"),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='changePassword.html', success_url='Success'), name='change_password'),
    path('change-password/Success/', change_password_success, name="changePasswordSuccess"),
]
#    path('changePassword/<int:id>', change_password, name="change_password"),

