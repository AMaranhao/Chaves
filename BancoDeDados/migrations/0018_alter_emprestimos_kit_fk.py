# Generated by Django 4.2.1 on 2023-07-11 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BancoDeDados', '0017_alter_cursosenac_nome_alter_funcionario_curso_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='Kit_FK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BancoDeDados.kits'),
        ),
    ]
