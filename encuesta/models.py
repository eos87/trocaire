# -*- coding: UTF-8 -*-
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from trocaire.lugar.models import *

class Encuestador(models.Model):
    nombre_completo = models.CharField(max_length=250, help_text='Un nombre y un Apellido')
    telefono = models.CharField(max_length=20, blank=True, default='')

    def __unicode__(self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = 'Encuestadores'

class Contraparte(models.Model):
    nombre = models.CharField(max_length=250)
    nombre_corto = models.CharField(max_length=50, blank=True, default='', verbose_name='SIGLAS')
    direccion = models.CharField(max_length=200, blank=True, default='')
    correo = models.EmailField(blank=True, default='')
    website = models.URLField(blank=True, default='')
    telefono = models.CharField(max_length=20, blank=True, default='')
    contacto = models.CharField(max_length=150, blank=True, default='')
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Contrapartes'

#Definiendo los choices
SEXOS = (('femenino', 'Femenino'), ('masculino', 'Masculino'))
ESTADO_CIVIL = (('soltero', 'Soltero/a'), ('casado', 'Casado/a'), ('acompanado', 'Unión de hecho estable'), ('no-aplica', 'No aplica'))
SI_NO = (('si', 'Si'), ('no', 'No'), ('no-aplica', 'No Aplica'))
SI_NO_SIMPLE = (('si', 'Si'), ('no', 'No'))
SI_NO_RESPONDE = ((1, 'Si'), (2, 'No'), (3, 'No sabe'), (4, 'No responde'))

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

SATISFECHAS = ((1, 'Bastante satisfechas'), (2, 'Poco satisfechas'), (3, 'Nada satisfechas'))

SERVICIOS = ((1, 'Buenos'), (2, 'Regulares'), (3, 'Deficientes'))

HOGAR = ((1, 'Siempre'), (2, 'Frecuentemente'), (3, 'A veces'), (4, 'Nunca'), (5, 'No aplica'))

COMUNICACION = ((1, 'De acuerdo'),
                (2, 'En desacuerdo'),
                (3, 'No sabe'),
                (4, 'No responde'))

class Base(models.Model):
    codigo = models.CharField(max_length=100)
    usuario = models.ForeignKey(User)
    fecha = models.DateField(verbose_name='Fecha de aplicación')
    sexo = models.CharField(max_length=30, choices=SEXOS)
    edad = models.IntegerField(help_text='Edad en años')
    comunidad = models.ForeignKey(Comunidad)
    municipio = models.ForeignKey(Municipio)
    estado_civil = models.CharField(choices=ESTADO_CIVIL, max_length=20)
    lugar_origen = models.CharField(max_length=200, blank=True, default='', verbose_name='Lugar de origen')
    asiste_iglesia = models.BooleanField(verbose_name='¿Asiste a alguna iglesia?')
    cual_iglesia = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        abstract = True
        ordering = ['-id']

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

    tiene_pareja = models.CharField(max_length=10, choices=SI_NO, verbose_name='1. Actualmente usted tiene esposo/a o compañero/a?')
    vive_con = models.ManyToManyField(ViveCon, verbose_name='En su hogar vive con:')
    cuantos_viven = models.IntegerField('Cuantas personas habitan en la casa donde usted vive?')
    entre0y6 = models.IntegerField('Número de niños entre 0 y 6 años que viven en la casa', blank=True, null=True)
    entre7y17 = models.IntegerField('Número de niños entre 0 y 17 años que viven en la casa', blank=True, null=True)
    entre18ymas = models.IntegerField('Número de personas de 18 y más años que viven en la casa', blank=True, null=True)
    tiene_hijos = models.CharField(max_length=10, choices=SI_NO)
    cuantos_hijos = models.IntegerField(verbose_name='¿Cuántos hijos tiene?', blank=True, null=True)
    #Hijos entre 0 y 6 años
    hijos0y6_mujeres = models.IntegerField('Mujeres', blank=True, null=True, default=0)
    hijos0y6_hombres = models.IntegerField('Hombres', blank=True, null=True, default=0)
    hijos7y17_mujeres = models.IntegerField('Mujeres', blank=True, null=True, default=0)
    hijos7y17_hombres = models.IntegerField('Hombres', blank=True, null=True, default=0)
    hijos18ymas_mujeres = models.IntegerField('Mujeres', blank=True, null=True, default=0)
    hijos18ymas_hombres = models.IntegerField('Hombres', blank=True, null=True, default=0)

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

#class padre de InformacionSocioEconomica para hereder elementos
class BaseInfoSocioEconomica(models.Model):
    estudia = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Estudia usted actualmente?')
    nivel_educativo = models.CharField(max_length=100, choices=NIVEL_EDUCATIVO, verbose_name='Cuál es su nivel educativo alcanzado?')
    
    class Meta:
        abstract = True

class InformacionSocioEconomica(BaseInfoSocioEconomica):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    
    trabaja_fuera = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Trabaja usted fuera del hogar?')
    donde_trabaja = models.ManyToManyField(LugarDeTrabajo, verbose_name='Donde trabaja?', blank=True, null=True)
    hace_dinero = models.IntegerField(choices=QUE_HACE_DINERO, verbose_name='Qué hace usted con el dinero que gana?', blank=True, null=True)
    aportan = models.ManyToManyField(Aporta, verbose_name='Quienes aportan ingresos en su hogar?')

    def __unicode__(self):
        return 'Info SocioEconomica %s' % self.id

    class Meta:
        verbose_name = 'Información socio-económica'
        verbose_name_plural = 'Información socio-económica'

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

    recursos = models.ManyToManyField(Recurso, related_name='recursos', verbose_name='Mencione los recursos de los cuales ud. es dueno/a', help_text=u'<b class=\'naranja\'>Si el encuestado no aplica a alguna opción, dejarla sin marcar.</b><br>', blank=True, null=True)
    recursos_decide = models.ManyToManyField(Recurso, related_name='recursos_decide', verbose_name='Mencione los recursos de los cuales ud. decide sobre el uso que les da', help_text=u'<b class=\'naranja\'>Si el encuestado no aplica a alguna opción, dejarla sin marcar.</b><br>', blank=True)

    def __unicode__(self):
        return 'Acceso y control %s' % self.id

    class Meta:
        verbose_name = 'Acceso y control de recursos'
        verbose_name_plural = 'Accesos y control de recursos'

class HablanDe(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Le hablan de'
        verbose_name_plural = 'Le hablan de'

class ConceptoViolencia(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    
    hablande = models.ForeignKey(HablanDe, verbose_name='Cuando alguien le habla de VBG, usted cree que están hablando de:', null=True)
    respuesta = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Seleccione la respuesta', null=True)

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

    justificacion = models.IntegerField(choices=JUSTIFICACIONES, verbose_name='Para Ud los hombres ejercen violencia hacia las mujeres porque:')
    respuesta = models.CharField(choices=SI_NO_SIMPLE, verbose_name='Seleccione la respuesta', max_length=10)

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
        return u'Situación de VBG %s' % self.id

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

CERO_SEIS = ((0, '1'),
             (1, '2'),
             (2, '3'),
             (3, '4'),
             (4, '5'),
             (5, '6'))
 
#class padre de Acciones ante una situación de VBG
class BaseAccionVBG(models.Model):
    ha_ayudado = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='En el último año Ud ha ayudado a alguna mujer que ha vivido VBG?')
    #campos de la pregunta que hace Ud?
    se_acerca = models.IntegerField(blank=True, null=True, verbose_name='Se acerca a la persona, la escucha y le brinda condiciones', choices=CERO_SEIS)
    invita_actividad = models.IntegerField(blank=True, null=True, verbose_name='La invita a una actividad colectiva en la que se habla sobre las causas y consecuencias de la VBG', choices=CERO_SEIS)
    no_hace_nada = models.IntegerField(blank=True, null=True, verbose_name='No hace nada por pena', choices=CERO_SEIS)
    no_hace_problema = models.IntegerField('No hace nada porque cree que eso es meterse en problemas', choices=CERO_SEIS, blank=True, null=True)
    busca_alternativa = models.IntegerField('Busca alternativas y le da seguimiento', choices=CERO_SEIS, blank=True, null=True)
    no_sabe = models.IntegerField('No sabe que hacer', choices=CERO_SEIS, blank=True, null=True)
    #terminan campos de que hace Ud?
    donde_buscar = models.ManyToManyField(BuscarAyuda, verbose_name=u'Dónde debe buscar ayuda una mujer que vive VBG?')
    accion_tomar = models.ManyToManyField(QueDebeHacer, verbose_name=u'Si un hombre le pega a su pareja, cuál de las siguientes acciones ella debería tomar?')    
    
    class Meta:
        abstract = True

#inline en esta shit
class AccionVBG(BaseAccionVBG):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return u'Accion ante VBG %s' % self.id

    class Meta:
        verbose_name = 'Acción ante situación de VBG'
        verbose_name_plural = 'Acciones ante situación de VBG'

class Quien(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Quien ejerció VBG'
        verbose_name_plural = 'Quienes ejercieron VBG'

class TipoVBG(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de VBG'
        verbose_name_plural = 'Tipo de VBG'

class PrevalenciaVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    ha_vivido_vbg = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='¿Considera Ud que alguna vez ha vivido VBG?')
    que_tipo = models.ManyToManyField(TipoVBG, verbose_name='¿Qué tipo de VBG ha vivido?', blank=True, null=True)
    frecuencia = models.IntegerField(choices=FRECUENCIA, verbose_name='En este último año, con qué frecuencia ha vivido situaciones de VBG', blank=True, null=True)
    quien = models.ManyToManyField(Quien, verbose_name=u'¿Quién es la persona que ha ejercido VBG sobre usted?', blank=True, null=True)

    def __unicode__(self):
        return 'Prevalencia de VBG %s' % self.id

    class Meta:
        verbose_name = 'Prevalencia de la VBG'
        verbose_name_plural = 'Prevalencias de la VBG'

#la VBG debe ser resuelta con ayuda de: esta es la tabla de valores a selccionar
class ResolverVBG(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'La VBG debe resolverse con'
        verbose_name_plural = 'La VBG de resolverse con'

class AsuntoPublicoVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    resolverse_con = models.ManyToManyField(ResolverVBG, verbose_name=u'¿Considera usted que la VBG es un asunto que debe ser resuelto con la participación de')

    def __unicode__(self):
        return u'VBG asunto público %s' % self.id

    class Meta:
        verbose_name = 'VBG como asunto público'
        verbose_name_plural = 'VBG como asunto público'

#tabla como afecta a las mujeres pag 9
class ComoAfecta(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Como afecta la VBG'
        verbose_name = 'Como afecta la VBG'

class EfectoVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    afecta_mujeres = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='¿Cree Ud que la VBG afecta a las mujeres, la familia y a la comunidad?')
    como_afecta = models.ManyToManyField(ComoAfecta, verbose_name=u'¿Cómo la VBG afecta a las mujeres, las familias y a las comunidades?', blank=True, null=True)

    def __unicode__(self):
        return 'Efecto VBG %s' % self.id

    class Meta:
        verbose_name = 'Efecto de la VBG'
        verbose_name_plural = 'Efectos de la VBG'

class ConocimientoLey(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    existe_ley = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='¿Sabe usted si en Nicaragua existe alguna ley que penaliza la violencia contra las mujeres')
    mencione = models.CharField(max_length=200, verbose_name='Puede mencionar el nombre de la ley que penaliza la Violencia contra las mujeres', blank=True, default='')

    #CAMPOS QUE VAN DENTRO DE UN FIELDSET
    padre_golpea = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Un padre o madre golpea a un hijo(a)', blank=True, default=4)
    maestro_castiga = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Un maestro o maestra que castiga física o psicologicamente a um alumno(a)', blank=True, default=4)
    maestro_relacion = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Un maestro o maestra que tiene relaciones sexuales con una alumna o un alumno', blank=True, default=4)
    joven_case = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Que un joven o una joven se case antes de los 18', blank=True, default=4)
    joven_relacion = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='2 personas menores de 18 años que tienen relaciones sexuales', blank=True, default=4)
    patron_acoso = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Un patrón que molesta/acosa sexualmente a una empleada', blank=True, default=4)
    lider_religioso = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Un líder religioso o comunitario que acosa sexualmente a una persona de su comunidad', blank=True, default=4)
    adulto_relacion = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Un adulto que sostiene relaciones con otra que es menor de edad', blank=True, default=4)
    adulto_dinero = models.IntegerField(choices=SI_NO_RESPONDE, verbose_name='Una persona adulta que ofrece dinero a una adolescente para tener relaciones sexuales', blank=True, default=4)


    def __unicode__(self):
        return 'Conocimiento de ley %s' % self.id

    class Meta:
        verbose_name = 'Conocimiento de Ley'
        verbose_name_plural = 'Conocimiento de leyes'

#clase para saber las decisiones a tomar
class Decision(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Decisiones'

class TomaDecision(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    decision = models.ManyToManyField(Decision, verbose_name=u'¿Cuando una mujer vive VBG cuales acciones deberia realizar?')

    def __unicode__(self):
        return u'Decisión %s' % self.id

    class Meta:
        verbose_name = 'Toma de decisión'
        verbose_name_plural = 'Toma de decisiones'

class Espacio(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Espacio comunitario'
        verbose_name_plural = 'Espacios Comunitarios'

class MotivoParticipacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Motivios de participación'

class ParticipacionPublica(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    espacio = models.ManyToManyField(Espacio, verbose_name=u'¿En qué organización o espacios comunitarios te encuentras integrada actualmente?')
    motivo = models.ManyToManyField(MotivoParticipacion, verbose_name=u'¿Qué le motiva a participar en esta organización?')

    def __unicode__(self):
        return u'Participación publica %s' % self.id

    class Meta:
        verbose_name = 'Participación Pública'
        verbose_name_plural = 'Participación Pública'

class IncidenciaPolitica(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    existen_mujeres = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='¿En su comunidad existen mujeres que representan a otras en espacios de participación ciudadana')
    satisfecha = models.IntegerField(choices=SATISFECHAS, verbose_name='¿Qué tan satisfechas cree Ud que están las mujeres de su comunidad con quienes las representan en esos espacios?', blank=True, null=True)

    def __unicode__(self):
        return u'Incidencia Política %s' % self.id

    class Meta:
        verbose_name_plural = 'Incidencia Política'

class TipoPropuesta(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name='Propuesta'
        verbose_name_plural='Propuestas'


class CalidadAtencion(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    valor_servicio = models.IntegerField(choices=SERVICIOS, verbose_name='¿Como valora Ud los servicios que las intituciones ofrecen a las mujeres que viven situaciones de VBG')
    #presentacion de propuestas
    propuesta = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Ha presentado propuestas ante las autoridades públicas para mejorar los servicios que brindan a mujeres en situaciones de VBG?')
    si_tipo = models.ManyToManyField(TipoPropuesta, verbose_name='¿Que tipo de propuesta ha presentado?', blank=True, null=True)
    no_porque = models.TextField(verbose_name='No ha presentado propuestas? Porque?', blank=True, default='')
    #negociacion de propuestas
    propuesta2 = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Ha negociado con las autoridades públicas alguna propuesta para mejorar los servicios que brindan a mujeres en situaciones de VBG?')
    si_tipo2 = models.ManyToManyField(TipoPropuesta, related_name='propuesta_negociada1', verbose_name='¿Qué propuestas ha negociado?', blank=True, null=True)
    no_porque2 = models.TextField(verbose_name='No ha negociado ninguna? Porque?', blank=True, default='')

    def __unicode__(self):
        return 'Calidad de atencion %s' % self.id

    class Meta:
        verbose_name_plural = u'Calidad de Atención'
        verbose_name = u'Calidad de Atención'

class Corresponsabilidad(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    lavar = models.IntegerField(choices=HOGAR, verbose_name='Lavar la ropa')
    plancar = models.IntegerField(choices=HOGAR, verbose_name='Planchar la ropa')
    limpiar = models.IntegerField(choices=HOGAR, verbose_name='Limpiar la casa')
    jalar_agua = models.IntegerField(choices=HOGAR)
    cuidar_ninos = models.IntegerField(choices=HOGAR, verbose_name='Cuidar a los niños y niñas')
    hacer_mandados = models.IntegerField(choices=HOGAR)
    llevar_lena = models.IntegerField(choices=HOGAR, verbose_name='Llevar la leña')
    lavar_trastes = models.IntegerField(choices=HOGAR, verbose_name='Lavar los trastes')
    arreglar_cama = models.IntegerField(choices=HOGAR, verbose_name='Arreglar la cama')
    ir_reuniones = models.IntegerField(choices=HOGAR, verbose_name='Ir a las reuniones en la escuela')
    acompanar = models.IntegerField(choices=HOGAR, verbose_name='Acompañar a los hijos/as en las tareas')
    hacer_compras = models.IntegerField(choices=HOGAR, verbose_name='Hacer las compras de la casa')
    pagar_servicios = models.IntegerField(choices=HOGAR, verbose_name='Pagar los sevicios públicos (agua, luz, etc.)')
    llevar_enfermos = models.IntegerField(choices=HOGAR, verbose_name='Llevar a los enfermos al médico/hospital')
    cuidar_enfermos = models.IntegerField(choices=HOGAR, verbose_name='Cuidar a los enfermos')

    def __unicode__(self):
        return 'Corresponsabilidad %s' % self.id

    class Meta:
        verbose_name = 'Corresponsabilidad en el hogar'
        verbose_name_plural = 'Corresponsabilidad en el hogar'

class SolucionConflicto(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Solución a conflicto'
        verbose_name_plural = 'Soluciones a conflicto'

class NegociacionExitosa(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Negociación exitosa'
        verbose_name_plural = 'Negociaciones exitosa'

DES_AC = ((1, 'De acuerdo'), (2, 'En desacuerdo'))

class ComunicacionAsertiva(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    #identifico = models.ManyToManyField(SolucionConflicto, verbose_name=u'¿Qué debo hacer para que la solución a un conflicto sea exitosa?')
    identificar = models.IntegerField(choices=DES_AC, verbose_name='Identifico claramente el conflicto y me pregunto porque ha pasado esto', null=True)
    analizar = models.IntegerField(choices=DES_AC, verbose_name='Analizo mis sentimientos y cuáles son los motivos de mi enojo', null=True)
    identificar_prioridad = models.IntegerField(choices=DES_AC, verbose_name='Identifico cuales son mis prioridades y que quiero conseguir', null=True)
    pido = models.IntegerField(choices=DES_AC, verbose_name='Le pido a la otra persona conversar sobre el tema manteniendo una actitud propositiva y no agresiva', null=True)
    actitud_pasiva = models.IntegerField(choices=DES_AC, verbose_name='Mantener una actitud pasiva y con contradecir o provocar a la otra persona', null=True)

    negociacion_exitosa = models.ManyToManyField(NegociacionExitosa, verbose_name=u'¿Qué se debe hacer para que una negociación de pareja sea exitosa?')

    def __unicode__(self):
        return u'Comunicación asertiva %s' % self.id

    class Meta:
        verbose_name = 'Comunicación asertiva'
        verbose_name_plural = 'Comunicaciones asertivas'

class Mujer(Base):
    encuestador = models.ForeignKey(Encuestador)
    contraparte = models.ForeignKey(Contraparte)
    composicion_hogar = generic.GenericRelation(ComposicionHogar)
    informacion_socio = generic.GenericRelation(InformacionSocioEconomica)
    acceso_recurso = generic.GenericRelation(AccesoControlRecurso)
    concepto_violencia = generic.GenericRelation(ConceptoViolencia)
    expresion_violencia = generic.GenericRelation(ExpresionVBG)
    creencia = generic.GenericRelation(Creencia)
    justificacion = generic.GenericRelation(JustificacionVBG)
    causa = generic.GenericRelation(CausaVBG)
    situacion = generic.GenericRelation(SituacionVBG)
    accionvbg = generic.GenericRelation(AccionVBG)
    #prevalencia cambia en hombres
    prevalencia = generic.GenericRelation(PrevalenciaVBG)
    asunto_publico = generic.GenericRelation(AsuntoPublicoVBG)
    efecto = generic.GenericRelation(EfectoVBG)
    conocimiento = generic.GenericRelation(ConocimientoLey)
    toma_decision = generic.GenericRelation(TomaDecision)
    participacion = generic.GenericRelation(ParticipacionPublica)
    incidencia = generic.GenericRelation(IncidenciaPolitica)
    calidad_atencion = generic.GenericRelation(CalidadAtencion)
    corresponsabilidad = generic.GenericRelation(Corresponsabilidad)
    comunicacion = generic.GenericRelation(ComunicacionAsertiva)
    
    def __unicode__(self):
        return u'Encuesta Mujeres %s' % self.id

    class Meta:        
        verbose_name = 'Encuesta Mujer'
        verbose_name_plural = 'Encuestas Mujeres'

class Quien2(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'A quien ejerció VBG'
        verbose_name_plural = 'A quienes ejerció VBG'


class PrevalenciaVBGHombre(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    ha_vivido_vbg = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='¿Considera Ud que alguna vez ha ejercido violencia hacia una mujer en el último año?')
    que_tipo = models.ManyToManyField(TipoVBG, verbose_name='¿Qué tipo de VBG ha ejercido?', blank=True, null=True)
    frecuencia = models.IntegerField(choices=FRECUENCIA, verbose_name='En este último año, con qué frecuencia ha ejercido violencia hacia mujer?', blank=True, null=True)
    quien = models.ManyToManyField(Quien2, verbose_name=u'¿Qué relación o parentesco tiene Ud con la mujer o mujeres contra las cuales ha ejercido violencia?', blank=True, null=True)

    def __unicode__(self):
        return 'Prevalencia de VBG %s' % self.id

    class Meta:
        verbose_name = 'Prevalencia de la VBG hombres'
        verbose_name_plural = 'Prevalencias de la VBG hombres'

class Hombre(Base):
    encuestador = models.ForeignKey(Encuestador)
    contraparte = models.ForeignKey(Contraparte)
    composicion_hogar = generic.GenericRelation(ComposicionHogar)
    informacion_socio = generic.GenericRelation(InformacionSocioEconomica)
    acceso_recurso = generic.GenericRelation(AccesoControlRecurso)
    concepto_violencia = generic.GenericRelation(ConceptoViolencia)
    expresion_violencia = generic.GenericRelation(ExpresionVBG)
    creencia = generic.GenericRelation(Creencia)
    justificacion = generic.GenericRelation(JustificacionVBG)
    causa = generic.GenericRelation(CausaVBG)
    situacion = generic.GenericRelation(SituacionVBG)
    accionvbg = generic.GenericRelation(AccionVBG)
    #prevalencia propia de hombres
    prevalencia = generic.GenericRelation(PrevalenciaVBGHombre)
    asunto_publico = generic.GenericRelation(AsuntoPublicoVBG)
    efecto = generic.GenericRelation(EfectoVBG)
    conocimiento = generic.GenericRelation(ConocimientoLey)
    toma_decision = generic.GenericRelation(TomaDecision)
    participacion = generic.GenericRelation(ParticipacionPublica)
    incidencia = generic.GenericRelation(IncidenciaPolitica)
    calidad_atencion = generic.GenericRelation(CalidadAtencion)
    corresponsabilidad = generic.GenericRelation(Corresponsabilidad)
    comunicacion = generic.GenericRelation(ComunicacionAsertiva)

    class Meta:
        verbose_name = 'Encuesta Hombre'
        verbose_name_plural = 'Encuestas Hombres'

    def __unicode__(self):
        return 'Encuesta Hombres %s' % self.id

class InformacionSocioEconomicaLider(BaseInfoSocioEconomica):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    trabaja_fuera = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='Trabaja usted fuera del hogar?')
    donde_trabaja = models.ManyToManyField(LugarDeTrabajo, verbose_name='Donde trabaja?', blank=True, null=True)

    def __unicode__(self):
        return 'Info SocioEconomica lideres %s' % self.id

    class Meta:
        verbose_name = 'Información socio-económica'
        verbose_name_plural = 'Información socio-económica'

SI_NO_SIMPLE2 = ((1, 'Si'), (2, 'No'))

class AccionPrevencion(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Acción para prevenir VBG'
        verbose_name_plural = u'Acciones para prevenir VBG'

class AccionVBGLider(BaseAccionVBG):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    ud_previene = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name=u'¿En su organización, escuela o usted realizan algunas acciones dirigidas a prevenir la VBG?')
    accion_prevenir = models.ManyToManyField(AccionPrevencion, blank=True, null=True, verbose_name=u'¿Cuáles son las acciones de prevención de violencia que su organización/escuela o usted ha desarrollado?')
    porque_no = models.TextField(blank=True, default='', verbose_name=u'¿Por qué no han realizado acciones dirigidas a prevenir la VBG?')

    def __unicode__(self):
        return 'Accion ante VBG %s' % self.id

    class Meta:
        verbose_name = 'Acción ante situación de VBG'
        verbose_name_plural = 'Acciones ante situación de VBG'

class PrevalenciaVBGLider(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    piensa_existe = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='¿Piensa Ud que en su comunidad existen mujeres que alguna vez han vivido VBG?')
    ha_vivido_vbg = models.CharField(max_length=10, choices=SI_NO_SIMPLE, verbose_name='¿Considera Ud que alguna vez ha vivido VBG?')
    que_tipo = models.ManyToManyField(TipoVBG, verbose_name='¿Qué tipo de VBG ha vivido?', blank=True, null=True)
    frecuencia = models.IntegerField(choices=FRECUENCIA, verbose_name='En este último año, con qué frecuencia ha vivido situaciones de VBG?', blank=True, null=True)
    quien = models.ManyToManyField(Quien, verbose_name=u'¿Quién es la persona que ha ejercido VBG sobre Ud?', blank=True, null=True)

    def __unicode__(self):
        return 'Prevalencia de VBG %s' % self.id

    class Meta:
        verbose_name = 'Prevalencia de la VBG lider'
        verbose_name_plural = 'Prevalencias de la VBG lider'

class Organizacion(models.Model):
    nombre = models.CharField(max_length=250)
    
    def __unicode__(self):
        return u'%s' % self.nombre
    
    class Meta:
        verbose_name_plural = 'Organizaciones'

class Lider(Base):
    encuestador = models.ForeignKey(Encuestador)
    contraparte = models.ForeignKey(Contraparte)
    organizacion = models.ForeignKey(Organizacion)
    cargo = models.CharField(max_length=150)
    informacion_socio = generic.GenericRelation(InformacionSocioEconomicaLider)
    concepto_violencia = generic.GenericRelation(ConceptoViolencia)
    expresion_violencia = generic.GenericRelation(ExpresionVBG)
    creencia = generic.GenericRelation(Creencia)
    justificacion = generic.GenericRelation(JustificacionVBG)
    causa = generic.GenericRelation(CausaVBG)
    situacion = generic.GenericRelation(SituacionVBG)
    accionvbg = generic.GenericRelation(AccionVBGLider)
    prevalencia = generic.GenericRelation(PrevalenciaVBGLider)
    asunto_publico = generic.GenericRelation(AsuntoPublicoVBG)
    efecto = generic.GenericRelation(EfectoVBG)
    conocimiento = generic.GenericRelation(ConocimientoLey)
    toma_decision = generic.GenericRelation(TomaDecision)
    incidencia = generic.GenericRelation(IncidenciaPolitica)
    calidad_atencion = generic.GenericRelation(CalidadAtencion)
    corresponsabilidad = generic.GenericRelation(Corresponsabilidad)
    comunicacion = generic.GenericRelation(ComunicacionAsertiva)

    class Meta:
        verbose_name = 'Encuesta Líder/Lideresa/Docente'
        verbose_name_plural = 'Encuesta Líderes/Lideresas/Docentes'

    def __unicode__(self):
        return 'Encuesta Lideres %s' % self.id

class Institucion(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = 'Instituciones'

class InformacionSocioEconomicaFuncionario(BaseInfoSocioEconomica):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return 'Info SocioEconomica %s' % self.id

    class Meta:
        verbose_name = 'Información socio-económica'
        verbose_name_plural = 'Información socio-económica'

FRECUENCIA_CAPAC = ((1, 'Una vez al año'), (2, 'Dos veces al año'), (3, 'Nunca'), (4, 'Otros'))
QUIEN_BRINDA = ((1, 'Estado'), (2, 'Sociedad Civil'), (3, 'Otros'))

class AccesoInformacion(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    recibe_capacitacion = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='¿Los funcionarios de la institución donde usted trabaja han recibido capacitación relacionada con la VBG?')
    frecuencia = models.IntegerField(choices=FRECUENCIA_CAPAC, verbose_name='¿Con que frecuencia han recibido estas capacitaciones?', blank=True, null=True)
    quien_brinda = models.IntegerField(choices=QUIEN_BRINDA, verbose_name='¿Quienes les brindan estas capacitaciones?', blank=True, null=True)

    def __unicode__(self):
        return u'Acceso a información %s' % self.id

    class Meta:
        verbose_name = u'Acceso a Información'
        verbose_name_plural = u'Acceso a Información'

CERO_CINCO = ((0, '1'),
             (1, '2'),
             (2, '3'),
             (3, '4'),
             (4, '5'))

class Instrumento(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Instrumentos'

class RutaCritica(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    pasos = models.BooleanField(verbose_name='¿Conoce los pasos de la ruta crítica de la violencia?')
    centro_mujeres = models.IntegerField(choices=CERO_CINCO, verbose_name='Centro de Mujeres en atención a Violencia', blank=True, null=True)
    centro_salud = models.IntegerField(choices=CERO_CINCO, verbose_name='Centro de salud / Medicina Legal', blank=True, null=True)
    comisaria = models.IntegerField(choices=CERO_CINCO, verbose_name='Comisaría de la mujer o policía', blank=True, null=True)
    juzgado = models.IntegerField(choices=CERO_CINCO, blank=True, null=True)
    ministerio_publico = models.IntegerField(choices=CERO_CINCO, verbose_name='Ministerio Público / Fiscalía', blank=True, null=True)
    instrumentos = models.ManyToManyField(Instrumento, verbose_name=u'Intrumentos')

    def __unicode__(self):
        return 'Ruta Crítica %s' % self.id

    class Meta:
        verbose_name_plural = 'Rutas Críticas'

class AccionVBGFuncionario(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    donde_buscar = models.ManyToManyField(BuscarAyuda, verbose_name=u'Dónde debe buscar ayuda una mujer que vive VBG?')
    accion_tomar = models.ManyToManyField(QueDebeHacer, verbose_name=u'Si un hombre le pega a su pareja, cuál de las siguientes acciones ella debería tomar?')

    def __unicode__(self):
        return 'Accion ante VBG %s' % self.id

    class Meta:
        verbose_name = 'Acción ante una situación de VBG'
        verbose_name_plural = 'Acciones ante una situación de VBG'

class RegistroDato(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    
    lleva_registro = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='Su institución lleva un registros de datos sobre los casos de VBG')
    cuantos = models.IntegerField(verbose_name='En el 2010, ¿Cuántos casos de VBG tienen registrados?', blank=True, default=0)
    #para hacer un fieldset los siguientes campos
    fisica = models.IntegerField(blank=True, default=0)
    sexual = models.IntegerField(blank=True, default=0)
    emocional = models.IntegerField(blank=True, default=0)
    sicologica = models.IntegerField(blank=True, default=0)
    otro = models.IntegerField(blank=True, default=0)
    
    def __unicode__(self):
        return 'Registro %s' % self.id

    class Meta:
        verbose_name = 'Registro de VBG'
        verbose_name_plural = 'Registros de VBG'

class CalidadAtencionFuncionario(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    valor_servicio = models.IntegerField(choices=SERVICIOS, verbose_name='¿Como valora Ud los servicios que las intituciones ofrecen a las mujeres que viven situaciones de VBG')

    def __unicode__(self):
        return 'Calidad de atencion %s' % self.id

    class Meta:
        verbose_name_plural = u'Calidad de Atención'
        verbose_name = u'Calidad de Atención'

class Accion(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Accion para mejorar'
        verbose_name = 'Acciones para mejorar'

class RecursoCuentaIns(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Recurso de la Institución'
        verbose_name_plural = 'Recursos de la Institución'

class AccionMejorarAtencion(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    realizo_accion = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='En el 2010, ¿realizó su institución algunas acciones dirigidas a mejorar la atención que brinda a mujeres en situación de VBG?')
    cuales = models.ManyToManyField(Accion, blank=True, null=True, verbose_name=u'¿Cuáles fueron las acciones dirigidas a mejorar la atención que brindan a mujeres en situación de VBG que su institución realizó?')
    recursos = models.ManyToManyField(RecursoCuentaIns, blank=True, null=True, verbose_name=u'¿Con que recursos cuenta su institución para realizar la atención que brinda a las mujeres que viven VBG?')

    def __unicode__(self):
        return 'Acción para mejorar atención %s' % self.id

    class Meta:
        verbose_name = 'Acción para mejorar atención'
        verbose_name_plural = 'Acciones para mejorar la atención'

class AccionPrevVBG(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    realizo_accion = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='En el 2010, ¿Realizó su institución algunas acciones dirigidas a prevenir la VBG?')
    accion_prevenir = models.ManyToManyField(AccionPrevencion, blank=True, null=True, verbose_name=u'¿Cuáles son las acciones de prevención de violencia que su organización/escuela o usted ha desarrollado?')

    def __unicode__(self):
        return 'Accion para prevención de VBG %s' % self.id

    class Meta:
        verbose_name = 'Acción para prevención de VBG'
        verbose_name_plural = 'Acciones para prevención de VBG'

class IncidenciaPoliticaFuncionario(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    ha_recibido = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='Su institución o Ud ha recibido propuestas que plantean mejorar los servicios que Uds brindan y/o realizar acciones de prevención de VBG de parte de las mujeres de las comunidades de este municipio?')
    que_comunidades = models.ManyToManyField(Comunidad, verbose_name=u'¿De que comunidades eran las mujeres que presentaron las propuestas?', blank=True, null=True)
    tipo_propuestas = models.ManyToManyField(TipoPropuesta, verbose_name=u'¿Que tipo de propuestas han recibido?', blank=True, null=True)
    ud_negociado = models.IntegerField(choices=SI_NO_SIMPLE2, verbose_name='¿Ud ha negociado con las mujeres de este municipio alguna propuesta que planteaba mejorar los servicios que Uds brindan a las mujeres que enfrentan VBG y/o la realización de acciones de prevención de VBG?')
    que_propuestas = models.ManyToManyField(TipoPropuesta, related_name='propuesta_negociada', blank=True, null=True, verbose_name=u'¿Qué tipo de propuestas han negociado?')

    def __unicode__(self):
        return 'Incidencia política %s' % self.id

    class Meta:
        verbose_name = 'Incidencia Política Funcionarios'
        verbose_name_plural = 'Incidencias Políticas Funcionarios'

class Funcionario(Base):
    encuestador = models.ForeignKey(Encuestador)
    contraparte = models.ForeignKey(Contraparte)
    institucion = models.ForeignKey(Institucion)
    cargo = models.CharField(max_length=150)
    informacion_socio = generic.GenericRelation(InformacionSocioEconomicaFuncionario)
    concepto_violencia = generic.GenericRelation(ConceptoViolencia)
    expresion_violencia = generic.GenericRelation(ExpresionVBG)
    creencia = generic.GenericRelation(Creencia)
    justificacion = generic.GenericRelation(JustificacionVBG)
    causa = generic.GenericRelation(CausaVBG)
    asunto_publico = generic.GenericRelation(AsuntoPublicoVBG)
    efecto = generic.GenericRelation(EfectoVBG)
    comunicacion = generic.GenericRelation(ComunicacionAsertiva)
    acceso_informacion = generic.GenericRelation(AccesoInformacion)
    conocimiento = generic.GenericRelation(ConocimientoLey)
    ruta_critica = generic.GenericRelation(RutaCritica)
    accionvbg = generic.GenericRelation(AccionVBGFuncionario)
    registro_dato = generic.GenericRelation(RegistroDato)
    calidad_atencion = generic.GenericRelation(CalidadAtencionFuncionario)
    mejorar_atencion = generic.GenericRelation(AccionMejorarAtencion)
    accion_prevencion = generic.GenericRelation(AccionPrevVBG)
    accion_prevencion = generic.GenericRelation(IncidenciaPoliticaFuncionario)

    class Meta:
        verbose_name = 'Encuesta Funcionaria/o'
        verbose_name_plural = 'Encuesta Funcionarias/os'

    def __unicode__(self):
        return 'Encuesta Funcionarias/os %s' % self.id
