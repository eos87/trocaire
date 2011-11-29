# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from trocaire.encuesta.models import *

urlpatterns = patterns('trocaire.mujeres_hombres.views',
    url(r'^$', 'index'),    
    url(r'^ha-presentado-propuestas/$', 'generic_view_hm', {'options': SI_NO_SIMPLE, 'field': 'propuesta', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'CalidadAtencion', 'titulo': u'¿Ha presentado propuestas ante autoridades públicas para mejorar los servicios que brindan a mujeres en situaciones de VBG?'}),
    
    url(r'^ha-negociado-propuestas/$', 'generic_view_hm', {'options': SI_NO_SIMPLE, 'field': 'propuesta2', 'template_name': 'monitoreo/generica_pie.html',
                                                            'modelo': 'CalidadAtencion', 'titulo': u'¿Ha negociado propuestas ante autoridades públicas para mejorar los servicios que brindan a mujeres en situaciones de VBG?'}),
    url(r'^(?P<vista>[-\w]+)/$', '_get_view'),    
)