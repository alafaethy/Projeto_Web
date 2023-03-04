# Generated by Django 4.1.7 on 2023-03-02 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_ticket_datatime_alter_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 2, 14, 24, 12, 253075)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='preco_mercado',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.FloatField(),
        ),
    ]