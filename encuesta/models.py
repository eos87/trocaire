from django.db import models

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

