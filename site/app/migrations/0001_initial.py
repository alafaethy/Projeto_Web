# Generated by Django 4.1.7 on 2023-02-17 17:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('datatime', models.DateTimeField(default=datetime.datetime(2023, 2, 17, 14, 22, 34, 817666))),
                ('nome_produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.produtos')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.vendedor')),
            ],
        ),
    ]
