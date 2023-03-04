# Generated by Django 4.1.7 on 2023-03-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_name_ticket_company_alter_ticket_cota_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='div_yield_ano',
            new_name='mercado_percente',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='proximo_rendimento',
            new_name='preco_mercado',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='ultimo_rendimento',
            new_name='px_rendimento',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='var_mercado_preco',
            new_name='rendimento',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='div_yield_mes',
            new_name='yld_ano',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='var_preco_porcento',
            new_name='yld_mes',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='datatime',
            field=models.DateTimeField(default='02-03-2023 14:13:18'),
        ),
    ]