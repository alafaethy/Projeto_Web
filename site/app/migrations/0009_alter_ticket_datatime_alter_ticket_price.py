# Generated by Django 4.1.7 on 2023-03-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_div_yield_ano_ticket_mercado_percente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='datatime',
            field=models.DateTimeField(default='02-03-2023 14:20:00'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
