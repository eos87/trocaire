# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^consultar/$', 'trocaire.encuesta.views.consultar'),

    url(r'^(?P<tipo>[-\w]+)/vbg-resolverse-con/$', 
        'trocaire.encuesta.views.generic_view', 
        {'model': 'asuntopublicovbg', 'options': 'resolvervbg', 'output': 'model', 'field': 'resolverse_con', 'titulo': u'¿Considera que la VBG es un asunto que debe ser resuelto con la participación de?'}, 
        name="vbg_resolver_con_func"),
    url(r'^(?P<tipo>[-\w]+)/como-afecta-vbg/$', 
        'trocaire.encuesta.views.generic_view', 
        {'model': 'efectovbg', 'options': 'comoafecta', 'output': 'model', 'field': 'como_afecta', 'titulo': u'¿Cómo la VBG afecta a las mujeres, las familias y a las comunidades?'}, 
        name="como_afecta_vbg_func"),                       
    url(r'^(?P<tipo>[-\w]+)/negociacion-exitosa-func/$', 
        'trocaire.encuesta.views.generic_view', 
        {'model': 'comunicacionasertiva', 'options': 'NegociacionExitosa', 'output': 'model', 'field': 'negociacion_exitosa', 'titulo': u'¿Qué se debe hacer para que una negociación de pareja sea exitosa?'}, 
        name="como_afecta_vbg_func"),    
    
    #---------------------lideres-------------------------------------     
    
    
    (r'^(?P<tipo>[-\w]+)/presenta-propuestas/$', 'trocaire.encuesta.views.presenta_propuestas'), 
    (r'^(?P<tipo>[-\w]+)/tipo-propuesta/$', 'trocaire.encuesta.views.tipo_propuesta_presentada'),
    
    (r'^lideres/$', direct_to_template, {'template': 'monitoreo/lideres.html'}),
    (r'^lideres/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_vista_lideres'),      
    
    (r'^funcionarios/$', direct_to_template, {'template': 'monitoreo/funcionarios.html'}),
    (r'^funcionarios/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_view_funcionario'),    
    
    (r'^(?P<tipo>[-\w]+)/$', 'trocaire.mujeres_hombres.views.index'),
    (r'^(?P<tipo>[-\w]+)/(?P<vista>[-\w]+)/$', 'trocaire.mujeres_hombres.views._get_view'),
)


