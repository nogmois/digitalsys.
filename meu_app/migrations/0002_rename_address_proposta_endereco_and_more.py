# Generated by Django 4.2.2 on 2023-06-15 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposta',
            old_name='address',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='proposta',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='proposta',
            old_name='amount',
            new_name='valor_emprestimo',
        ),
    ]
