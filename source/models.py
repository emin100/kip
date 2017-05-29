# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.


class Machine(models.Model):
    machine_name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.BinaryField()
    port = models.SmallIntegerField()
    state = models.BooleanField()

    machine_type = models.ForeignKey('MachineType', models.DO_NOTHING, default=1)
    machine_kind = models.ForeignKey('MachineKind', models.DO_NOTHING, default=1)

    def __unicode__(self):
        return self.machine_name

    class Meta:
        managed = True
        db_table = "machine"
        verbose_name = _('machine')
        verbose_name_plural = _(verbose_name)


class MachineKind(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    kind = models.CharField(max_length=150)
    state = models.BooleanField()

    def __unicode__(self):
        return self.kind

    class Meta:
        managed = True
        db_table = 'machine_kind'
        verbose_name = _('Machine Kind')
        verbose_name_plural = _(verbose_name)


class MachineType(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    state = models.BooleanField()

    def __unicode__(self):
        return self.type

    class Meta:
        managed = True
        db_table = 'machine_type'
        verbose_name = _('machine type')
        verbose_name_plural = _(verbose_name)
