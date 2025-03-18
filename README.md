# Sobre o projeto
## Objetivo
    O objetivo do projeto é gerenciar o emprestimo de chaves e agendamento de salas de uma faculdade
####   PS: Projeto ainda em andamento, faltando a criação de emprestimos

## Tecnologias
* Python 3.11
* PostgreSQL 15
* Django 4.1

## Como executar
1. Instalar o PostgreSQL
   1. criar o schema `gestao_chaves`
   2. no arquivo gestaoChaves/.env
      1. definir o usuário do banco de dados
      2. definir a senha do banco de dados
2. Instalar o Python 3.11
3. Clonar repositório para maquina local
4. Com o terminal na pasta do arquivo clonado, digitar os comandos:
   1. `python -m venv venv` para criar a virtual env
   2. Ativar a virtual env
      1. `source venv/bin/activate` caso esteja no macOS
      2. `.\venv\Scripts\activate` caso esteja no windows
5. `pip install -r requirements-dev.txt` para instalar todas as bibliotecas necessárias
6. Utilizar comandos `python3 manage.py migrate` e `python3 manage.py makemigrations`
7. Utilizar o comando `python3 manage.py runserverr` para rodar o aplicativo
8. Clicar no link para utilizar o aplicativo
9. É necessário usar o super user no django admin para criar nesta ordem:
a)Inserir predio
b)Inserir cursos
c)Inserir tipos de sala
d)Inserir salas
e)Inserir kits (opcional)
f)Inserir chaves
g)Inserir um cursosenac
h)Inserir um coordenador
10. Testar o sistema
      