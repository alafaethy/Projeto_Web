# Generated by Django 4.1.7 on 2023-02-17 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_vendas_datatime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 17, 15, 9, 18, 523400)),
        ),
    ]