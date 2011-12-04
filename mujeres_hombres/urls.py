# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from trocaire.encuesta.models import *

RANGOS = (([1, 2], 'De 1 a 2'), ([3, 4], 'De 3 a 4'),
          ([5, 6], 'De 5 a 6'), ([7, 8], 'De 7 a 8'),
          ([9, 10], 'De 9 a 10'), ([11, 2000], 'Más de 10'))

PERSONAS_HABITAN = (('entre0y6', u'Número de niños entre 0 y 6 años'), 
                    ('entre7y17', u'Número de niños entre 7 y 17 años'), 
                    ('entre18ymas', u'Número de personas de 18 y más años'))

HIJOS_HOMBRES = (('hijos0y6_hombres', u'Número de niños entre 0 y 6 años'),
                 ('hijos7y17_hombres', u'Número de niños entre 7 y 17 años'),
                 ('hijos18ymas_hombres', u'Número de personas de 18 y más años'))

HIJAS_MUJERES = (('hijos0y6_mujeres', u'Número de niños entre 0 y 6 años'),
                 ('hijos7y17_mujeres', u'Número de niños entre 7 y 17 años'),
                 ('hijos18ymas_mujeres', u'Número de personas de 18 y más años'))

urlpatterns = patterns('trocaire.mujeres_hombres.views',
    url(r'^$', 'index'),    
    url(r'^ha-presentado-propuestas/$', 'generic_view_hm', {'options': SI_NO_SIMPLE, 'field': 'propuesta', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'CalidadAtencion', 'titulo': u'¿Ha presentado propuestas ante autoridades públicas para mejorar los servicios que brindan a mujeres en situaciones de VBG?'}),    
    url(r'^ha-negociado-propuestas/$', 'generic_view_hm', {'options': SI_NO_SIMPLE, 'field': 'propuesta2', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'CalidadAtencion', 'titulo': u'¿Ha negociado propuestas ante autoridades públicas para mejorar los servicios que brindan a mujeres en situaciones de VBG?'}),
    url(r'^vive-con/$', 'generic_view_hm', {'options': ViveCon.objects.all(), 'field': 'vive_con', 'template_name': 'monitoreo/generica_1.html',
                                                            'modelo': 'ComposicionHogar', 'titulo': u'¿En su hogar usted vive con?'}),
    url(r'^cuantos-viven/$', 'generic_view_hm', {'options': RANGOS, 'field': 'cuantos_viven__range', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'ComposicionHogar', 'titulo': u'¿Cuántas personas habitan en la casa donde usted vive?'}),                   
    url(r'^tiene-hijos/$', 'generic_view_hm', {'options': SI_NO, 'field': 'tiene_hijos', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'ComposicionHogar', 'titulo': u'¿Tiene usted hijos e hijas?'}),
    url(r'^cuantos-hijos/$', 'generic_view_hm', {'options': RANGOS, 'field': 'cuantos_hijos__range', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'ComposicionHogar', 'titulo': u'¿Cuántos hijos tiene usted?', 'nocheck': True}),
    url(r'^estudia-actualmente/$', 'generic_view_hm', {'options': SI_NO_SIMPLE, 'field': 'estudia', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'InformacionSocioEconomica', 'titulo': u'¿Estudia actualmente?'}),
    url(r'^donde-trabaja/$', 'generic_view_hm', {'options': LugarDeTrabajo.objects.all(), 'field': 'donde_trabaja', 'template_name': 'monitoreo/generica_1.html',
                                                            'modelo': 'InformacionSocioEconomica', 'titulo': u'¿Donde Trabaja?'}),
    #------------
    url(r'^cantidad-personas/$', 'cantidad_personas', {'options': PERSONAS_HABITAN, 'modelo': 'ComposicionHogar', 'graph_title': u'Promedio de personas que habitan en la casa', 
                                                       'titulo': u'Cantidad de personas que habitan en la casa', }),
    url(r'^hijos-hombres/$', 'cantidad_personas', {'options': HIJOS_HOMBRES, 'modelo': 'ComposicionHogar', 'graph_title': u'Promedio de hijos hombres que viven en la casa', 
                                                       'titulo': u'Cantidad hijos hombres viven con usted', }),
    url(r'^hijas-mujeres/$', 'cantidad_personas', {'options': HIJAS_MUJERES, 'modelo': 'ComposicionHogar', 'graph_title': u'Promedio de hijas mujeres que viven en la casa', 
                                                       'titulo': u'Cantidad hijas mujeres viven con usted', }),
    url(r'^mencione-leyes/$', 'lista_generica', {'modelo': 'ConocimientoLey', 'field': 'mencione', 'titulo': u'Mencione la ley que penaliza la VBG contra las mujeres'}),
    url(r'^propuestas-presentadas/$', 'lista_generica', {'modelo': 'CalidadAtencion', 'options': TipoPropuesta.objects.all(), 'field': 'si_tipo__in', 
                                                         'titulo': u'Que tipo de propuestas ha presentado', 'field_values': 'si_tipo__nombre'}),
    url(r'^propuestas-negociadas/$', 'lista_generica', {'modelo': 'CalidadAtencion', 'options': TipoPropuesta.objects.all(), 'field': 'si_tipo2__in', 
                                                         'titulo': u'Que tipo de propuestas ha negociado', 'field_values': 'si_tipo2__nombre'}),
    
    url(r'^(?P<vista>[-\w]+)/$', '_get_view'),    
)