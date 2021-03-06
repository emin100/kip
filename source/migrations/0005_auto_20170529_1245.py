# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0004_auto_20170529_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineKind',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=150)),
                ('state', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Machine Kind',
                'db_table': 'machine_kind',
                'managed': True,
                'verbose_name_plural': 'Machine Kind',
            },
        ),
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('state', models.BooleanField()),
            ],
            options={
                'verbose_name': 'machine type',
                'db_table': 'machine_type',
                'managed': True,
                'verbose_name_plural': 'machine type',
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_kind',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='source.MachineKind'),
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='source.MachineType'),
        ),
    ]
