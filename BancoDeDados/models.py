from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime

class PREDIO(models.Model):
    Nome = models.CharField(max_length=20)
    Endereco = models.CharField(max_length=60, null=True)
    Telefone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.Nome


class TIPO_SALA(models.Model):
    Tipo_Sala = models.CharField(max_length=20)

    def __str__(self):
        return self.Tipo_Sala


class SALAS(models.Model):
    Numero = models.CharField(max_length=4)
    Tipo_de_Kit = models.CharField(max_length=4)
    Tipo_Sala_FK = models.ForeignKey(TIPO_SALA, on_delete=models.CASCADE)
    Ocupada = models.BooleanField(default=False)
    Esta_ativa = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.Numero


class CHAVES(models.Model):
    Numero = models.CharField(max_length=4)
    Numeracao_Armario = models.CharField(max_length=4)
    Salas_FK = models.ForeignKey(SALAS, on_delete=models.CASCADE)

    def __str__(self):
        return self.Numero


class KITS(models.Model):
    Numero = models.CharField(max_length=4)
    Numeracao_Armario = models.CharField(max_length=4)
    Tipo_de_Kit = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.Numero} - {self.Tipo_de_Kit}"


class CARGO(models.Model):
    Nome = models.CharField(max_length=20)

    def __str__(self):
        return self.Nome


class CURSOSENAC(models.Model):
    Nome = models.CharField(max_length=20)
    Codigo = models.CharField(max_length=8)
    Predio_FK = models.ForeignKey(PREDIO, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome




class FUNCIONARIO(models.Model):
    CPF = models.CharField(max_length=14, unique=True)
    Matricula = models.CharField(max_length=15, unique=True)
    Telefone = models.CharField(max_length=11)
    User_FK = models.OneToOneField(User, on_delete=models.CASCADE)
    Curso_FK = models.ForeignKey(CURSOSENAC, on_delete=models.CASCADE)
    Cargo_FK = models.ForeignKey(CARGO, on_delete=models.CASCADE)

    def __str__(self):
        return self.User_FK.username



class EMPRESTIMOS(models.Model):
    Funcionario_FK = models.ForeignKey(FUNCIONARIO, on_delete=models.CASCADE)
    Chaves_FK = models.ForeignKey(CHAVES, on_delete=models.CASCADE)
    Kit_FK = models.ForeignKey(KITS, on_delete=models.CASCADE, null=True)
    Horario_Recepcao = models.DateTimeField()
    Horario_Devolucao = models.DateTimeField(null=True, blank=True)
    Esta_Emprestado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Funcionario_FK} - {self.Horario_Recepcao} - {self.Horario_Devolucao}"



class AGENDAMENTO(models.Model):
    Funcionario_FK = models.ForeignKey(FUNCIONARIO, on_delete=models.CASCADE)
    Horario_inicio = models.DateTimeField()
    Horario_fim = models.DateTimeField()
    Kit = models.BooleanField(default=False)
    Salas_FK = models.ForeignKey(SALAS, on_delete=models.CASCADE)
    EstaAgendado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Funcionario_FK} - {self.Salas_FK} - {self.Horario_inicio} - {self.Horario_fim}"




# Inserindo dados para testes
