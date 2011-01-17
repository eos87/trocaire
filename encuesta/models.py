# -*- coding: UTF-8 -*-
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
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

#Definiendo los choices
SEXOS = (('femenino', 'Femenino'), ('masculino', 'Masculino'))
ESTADO_CIVIL = (('soltero', 'Soltero/a'), ('casado', 'Casado/a'), ('no-aplica', 'No aplica'))
SI_NO = (('si', 'Si'), ('no', 'No'), ('no-aplica', 'No Aplica'))
SI_NO_SIMPLE = (('si', 'Si'), ('no', 'No'))
NIVEL_EDUCATIVO = (('primaria-completa', 'Primaria Completa'),
                   ('primaria-incompleta', 'Primaria Incompleta'),
                   ('secundaria-completa', 'Secundaria Completa'),
                   ('secundaria-incompleta', 'Secundaria Incompleta'),
                   ('tecnico', 'Técnico o Tecnólogo'),
                   ('universitario-sin-titulo', 'Superior o Universitario sin título'),
                   ('universitario-con-titulo', 'Superior o Universitario con título'),
                   ('postgrado', 'Postgrado'),
                   ('ninguno', 'Ninguno'))

QUE_HACE_DINERO = ((1, 'Lo guarda y decide como utilizarlo'),
                   (2, 'Da una parte a su pareja voluntariamente'),
                   (3, 'Da una parte a su pareja en contra de su voluntad'),
                   (4, 'Da todo a su mama'),
                   (5, 'Da todo a su papa'))

MANERAS_VBG = ((1, 'Golpes a las Mujeres'),
               (2, 'Palabras y miradas que humillan, ridiculización, palabras groseras y gritos hacia las mujeres'),
               (3, 'Amenazas y Chantajes'),
               (4, 'Cuando la mujer tiene que pedir permiso para visitar a su familiares'),
               (5, 'Cuando hay preferencias para que estudie el varón'),
               (6, 'Cuando la mujer tiene que obedecer a su marido'),
               (7, 'Cuando la mujer aunque no tenga deseos, es obligada por su pareja a tener relaciones sexuales'),
               (8, 'Cuando solo el hombre quiere progresar y no se lo permite a la mujer'),
               (9, 'Cuando el hombre no valora los logros de la mujer'),
               (10, 'Cuando la mujer es celada por su pareja'),
               (11, 'Cuando el marido empuja a su esposa por no estar de acuerdo con ella'),
               (12, 'Obligar a la mujer a tener relaciones sexuales sin protección anticonceptiva o contra ITS'),
               (13, 'Hacer que la mujer tenga que pedirle dinero a su marido y rendirle cuenta sobre como lo gastó'),
               (14, 'Cuando el hombre tiene a su nombre las propiedades obtenidas durante el matrimonio o decide a quien dársela'),
               (15, 'Cuando el hombre no permite que la mujer salga a divertirse con sus amigos/as sin hijos/as'),
               (16, 'Cuando el hombre no le permite a la mujer que se organice y participe en actividades comunitarias'),
               (17, 'Cuando tu papa o mama no te permite organizarte y participar en actividades comunitarias'))

CREENCIAS_VBG = ((1, 'Una buena esposa obedece a su esposo aunque ella tenga otra opción'),
                 (2, 'Los problemas familiares solo deben discutirse con miembros de la familia'),
                 (3, 'Es importante para el hombre demostrarle a su pareja quien manda'),
                 (4, 'Una mujer debe estar en capacidad de escoger a sus amistades aunque su esposo esté en desacuerdo'),
                 (5, 'Es obligación de la esposa tener relaciones sexuales con su esposo aunque no sienta deseos'),
                 (6, 'Si un hombre maltrata a su esposa, otras personas ajenas a la familia deben intervenir'))

CREENCIAS_VBG_RESP = ((1, 'De acuerdo'),
                      (2, 'En desacuerdo'),
                      (3, 'No sabe'),
                      (4, 'No responde'))

JUSTIFICACIONES = ((1, 'Beben Licor'),
                   (2, 'La addicción a las drogas'),
                   (3, 'El estrés por estar desempleados'),
                   (4, 'La pobreza'),
                   (5, 'El hombre ha sido víctima de malos tratos en la niñez'),
                   (6, 'Ya nace violento'),
                   (7, 'Por que las mujeres no le hacen caso a su marido'),
                   (8, 'El bajo nivel educativo de los hombres'),
                   (9, 'La influencia de la familia'),
                   (10, 'Las creencias religiosas'),
                   (11, 'El comportamiento provocador de las mujeres'),
                   (12, 'Otros'))

CAUSAS_VBG = ((1, 'Que las mujeres son consideradas como un objeto'),
              (2, 'La crianza y el tipo de educación que han recibido'),
              (3, 'Al machismo'),
              (4, 'Que los hombres tienen ese derecho'),
              (5, 'La influencia de los medios de comunicación'),
              (6, 'La influencia religiosa que promueve la obediencia de la mujer al hombre'),
              (7, 'Al desconocimiento de las mujeres de sus derechos'),
              (8, 'Que culturalmente es aceptado que los hombres controlen y dominen a las mujeres'))

QUE_HACE = ((1, 'Se acerca a la persona, la escucha y le brinda orientaciones sobre qué hacer'),
            (2, 'La invita a una actividad colectiva en la que se habla sobre las causas y consecuencias de la VBG'),
            (3, 'No hace nada por pena'),
            (4, 'No hace nada porque cree que eso es meterse a problemas'),
            (5, 'Busca alternativas y le da seguimiento'),
            (6, 'No sabe que hacer'))

TIPO_VBG = ((1, 'Física'),
            (2, 'Sexual'),
            (3, 'Emocional'),
            (4, 'Psicológica'),
            (5, 'Otro'))

FRECUENCIA = ((1, 'A diario'),
              (2, 'Una vez a la semana'),
              (3, 'Una vez al mes'),
              (4, 'Más de una vez al mes'))

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

class ViveCon(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Persona con quien vive'
        verbose_name_plural = 'Personas con quien vive'


class ComposicionHogar(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    tiene_pareja = models.CharField(max_length=10, choices=SI_NO, verbose_name='Actualmente usted tiene esposo/a o compañero/a?')
    vive_con = models.ManyToManyField(ViveCon)
    cuantos_viven = models.IntegerField('Cuantas personas habitan en la casa donde usted vive?')
    entre0y6 = models.IntegerField('Número de niños entre 0 y 6 años que viven en la casa', default=0)
    entre7y17 = models.IntegerField('Número de niños entre 0 y 17 años que viven en la casa', default=0)
    entre18ymas = models.IntegerField('Número de personas de 18 y más años que viven en la casa', default=0)
    tiene_hijos = models.CharField(max_length=10, choices=SI_NO)
    hijos0y6 = models.IntegerField('Hijos entre 0 y 6 años', default=0)
    hijos7y17 = models.IntegerField('Hijos entre 0 y 17 años', default=0)
    hijos18ymas = models.IntegerField('Hijos entre  18 y más', default=0)

    class Meta:
        verbose_name = 'Composición del Hogar'
        verbose_name_plural = 'Composición del Hogar'

    def __unicode__(self):
        return 'Composicion %s' % self.id

class LugarDeTrabajo(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Lugares de trabajo'

    def __unicode__(self):
        return self.nombre

class Aporta(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Aportan'

class InformacionSocioEconomica(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    estudia = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Estudia usted actualmente?')
    nivel_educativo = models.CharField(max_length=100, choices=NIVEL_EDUCATIVO, verbose_name='Cuál es su nivel educativo alcanzado?')
    trabaja_fuera = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Trabaja usted fuera del hogar?')
    donde_trabaja = models.ManyToManyField(LugarDeTrabajo, verbose_name='Donde trabaja?')
    hace_dinero = models.IntegerField(choices=QUE_HACE_DINERO, verbose_name='Qué hace usted con el dinero que gana?')
    aportan = models.ManyToManyField(Aporta, verbose_name='Quienes aportan ingresos en su hogar?')

    def __unicode__(self):
        return 'Info SocioEconomica %s' % self.id

class Recurso(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Recursos'

class AccesoControlRecurso(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    recursos = models.ManyToManyField(Recurso, verbose_name='Mencione los recursos de los cuales ud. es dueño/a')
    recursos_decide = models.ManyToManyField(Recurso, related_name='recursos-decide', verbose_name='Menciones los recursos de los cuales ud. decide sobre el uso que les da')

    def __unicode__(self):
        return 'Acceso y control %s' % self.id

    class Meta:
        verbose_name = 'Acceso y control de recursos'
        verbose_name_plural = 'Accesos y control de recursos'

class VBG(models.Model):
    nombre = models.CharField(max_lenth=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'VBGs'

class ConceptoViolencia(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    conocimientoVBG = models.ManyToManyField(VBG, verbose_name='Cuando alguien le habla de VBG, usted cree que están hablando de:')

    def __unicode__(self):
        return 'Conocimiento de Violencia %s' % self.id

    class Meta:
        verbose_name_plural = 'Conceptos de Violencia'

class ExpresionVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    maneras = models.IntegerField(choices=MANERAS_VBG, verbose_name='De que manera considera que se expresa la VBG?')
    respuesta = models.CharField(max_length=20, choices=SI_NO, verbose_name='Seleccione la respuesta')

    def __unicode__(self):
        return 'Expresion de VBG %s' % self.id

    class Meta:
        verbose_name = 'Expresión de VBG'
        verbose_name_plural = 'Expresiones de VBG'

class Creencia(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    creencia = models.IntegerField(choices=CREENCIAS_VBG, verbose_name='Creencias sobre cómo deben comportarse hombres y mujeres')
    respuesta = models.IntegerField(choices=CREENCIAS_VBG_RESP)

    def __unicode__(self):
        return 'Creencias %s' % self.id

    class Meta:
        verbose_name_plural = 'Creencias'

class JustificacionVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    justificacion = models.IntegerField(choices=JUSTIFICACIONES, verbose_name='Para Ud los hombres efercen violencia hacia las mujeres porque:')
    respuesta = models.CharField(choices=SI_NO_SIMPLE, verbose_name='Seleccione la respuesta')

    def __unicode__(self):
        return 'Justificacion VBG %s' % self.id

    class Meta:
        verbose_name = 'Justificación de la VBG'
        verbose_name_plural = 'Justificaciones de la VBG'

class CausaVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    causa = models.IntegerField(choices=CAUSAS_VBG, verbose_name='Cree usted que los hombres son violentos debido a:')
    respuesta = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Seleccione la respuesta')

    def __unicode__(self):
        return 'Causa de la VBG %s' % self.id

    class Meta:
        verbose_name = 'Causa de la VBG'
        verbose_name_plural = 'Causas de la VBG'

class SituacionVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    conoce_hombres = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Conoce usted si en su comunidad existen hombres que ejercen VBG?')
    conoce_mujeres = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Conoce usted si en su comunidad hay mujeres que alguna vez han vivido VBG?')

    def __unicode__(self):
        return 'Situación de VBG %s' % self.id

    class Meta:
        verbose_name = 'Identificación de situación de VBG'
        verbose_name_plural = 'Identificación de situaciones de VBG'

#donde busca ayuda en caso de VBG
class BuscarAyuda(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Donde buscar ayuda'
        verbose_name_plural = 'Donde buscar ayuda'

#que debe hacer la mujer en caso de VBG
class QueDebeHacer(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Que hacer si sufre VBG'
        verbose_name_plural = 'Que hacer si sufre VBG'

#inline en esta shit
class AccionVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    ha_ayudado = models.InterField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='En el último año Ud ha ayudado a alguna mujer que ha vivido VBG?')
    donde_buscar = models.ManyToManyField(BuscarAyuda, verbose_name='Dónde debe buscar ayuda una mujer que vive VBG')
    accion_tomar = models.ManyToManyField(QueDebeHacer, verbose_name='Si un hombre le pega a su pareja, cuál de las siguientes acciones ella debería tomar')

    def __unicode__(self):
        return 'Accion ante VBG %s' % self.id

    class Meta:
        verbose_name = 'Acción ante situación de VBG'
        verbose_name_plural = 'Acciones ante situación de VBG'

#clase para la pregunta anterior. Tener en cuenta el fuckin inline
class QueHaceUd(models.Model):
    accionvbg = models.ForeignKey(AccionVBG)
    que_hace = models.IntegerField(choices=QUE_HACE, verbose_name='Qué hace usted cuando existe una situación de violencia basada en género en su comunidad?')

    def __unicode__(self):
        return 'Que hace Ud %s' % self.id

    class Meta:
        verbose_name = 'Que hace Ud en caso de VBG'
        verbose_name_plural = 'Que hace Ud en caso de VBG'

class Quien(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Quien ejerció VBG'
        verbose_name_plural = 'Quienes ejercieron VBG'

class PrevalenciaVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    ha_vivido_vbg = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='¿Considera Ud que alguna vez ha vivido VBG?')
    que_tipo = models.IntegerField(choices=TIPO_VBG, verbose_name='¿Qué tipo de VBG ha vivido?')
    frecuencia = models.IntegerField(choices=FRECUENCIA, verbose_name='En este último año, con qué frecuencia ha vivido situaciones de VBG')
    quien = models.ManyToManyField(Quien, verbose_name='¿Quién es la persona que ha ejercido VBG sobre usted?')

    def __unicode__(self):
        return 'Prevalencia de VBG %s' % self.id

    class Meta:
        verbose_name = 'Prevalencia de la VBG'
        verbose_name_plural = 'Prevalencias de la VBG'
