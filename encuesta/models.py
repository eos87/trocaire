# -*- coding: UTF-8 -*-
from django.db import models
from trocaire.lugar.models import *

class Encuestador(models.Model):
     nombre_completo = models.CharField(max_length=250, help_text='Un nombre y un Apellido')
     telefono = models.CharField(max_length=20, blank=True, defatult='')

     def __unicode__(self):
         return self.nombre_completo

     class Meta:
         verbose_name_plural = 'Encuestadores'

class Contraparte(models.Model):
    nombre = models.CharField(max_length=250)
    nombre_corto = models.CharField(max_length=50, blank=True, default='')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Contrapartes'

SEXOS = (('femenino', 'Femenino'), ('masculino', 'Masculino'))
ESTADO_CIVIL = (('soltero', 'Soltero/a'), ('casado', 'Casado/a'), ('no-aplica', 'No aplica'))

class Base(models.Model):
    sexo = models.CharField(max_length=30, choices=SEXOS)
    edad = models.IntegerField(help_text='Edad en años')
    comunidad = models.ForeignKey(Comunidad)
    municipio = models.ForeignKey(Municipio)
    estado_civil = models.CharField(choices=ESTADO_CIVIL)
    lugar_origen = models.CharField(max_length=200, blank=True, default='')
    asiste_iglesia = models.BooleanField()
    cual_iglesia = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        abstract = True
        ordering = ['-id']


class Mujer(Base):
    class Meta:
        verbose_name = 'Encuesta Mujer'
        verbose_name_plural = 'Encuestas Mujeres'
