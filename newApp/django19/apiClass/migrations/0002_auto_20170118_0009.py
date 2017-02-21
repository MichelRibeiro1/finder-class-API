# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-18 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiClass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=200)),
                ('semestre', models.CharField(max_length=2)),
                ('curso', models.CharField(max_length=200)),
                ('dia_aula', models.CharField(max_length=5)),
                ('hora_inicio', models.CharField(max_length=10)),
                ('hora_fim', models.CharField(max_length=10)),
                ('codigo', models.CharField(max_length=10)),
                ('lixo', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Whatever',
        ),
    ]
