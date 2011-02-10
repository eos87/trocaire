# -*- coding: UTF-8 -*-

from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

class Departamento(models.Model):
    pais = models.ForeignKey(Pais)
    id = models.IntegerField("Código", primary_key=True)
    nombre = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, null=True, help_text="Usado como url unica(autorellenado)")
    extension = models.DecimalField("Extension Territorials", max_digits=10, decimal_places=2, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos/Provincias"

class Municipio(models.Model):
    id = models.IntegerField("Código", primary_key=True)
    departamento = models.ForeignKey(Departamento, blank=True, null=True)
    nombre = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=True, help_text="Usado como url unica(autorellenado)")
    extension = models.DecimalField("Extension Territorial", max_digits=10, decimal_places=2, blank=True, null=True)
    latitud = models.DecimalField('Latitud', max_digits=8, decimal_places=5, blank=True, null=True)
    longitud = models.DecimalField('Longitud', max_digits=8, decimal_places=5, blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.departamento.nombre, self.nombre)

    class Meta:
        verbose_name_plural = "Municipios/Cantones"
        ordering = ['departamento__nombre', ]

class Comunidad(models.Model):
    municipio = models.ForeignKey(Municipio)
    #microcuenca = models.ForeignKey(Microcuenca,null=True,blank=True)
    nombre = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural="Comunidad"

    def __unicode__(self):
        return self.nombre
