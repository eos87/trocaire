# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from models import FRECUENCIA_CAPAC

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
    
    #------------------ ha presentado y ha negociado propuestas ---------------------    
    url(r'^lideres/presenta-propuestas/$', 
        'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'lideres', 'model': 'calidadatencion', 'options': ['si', 'no'], 'tipo_choice': 'si_no', 'field': 'propuesta', 'titulo': u'¿Ha presentado propuestas de acciones de prevención de VBG?'}, 
        name="presenta_lideres"),
    url(r'^funcionarios/presenta-propuestas/$', 
        'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'funcionarios', 'model': 'IncidenciaPoliticaFuncionario', 'options': ['si', 'no'], 'tipo_choice': 'simple', 'field': 'ha_recibido', 'titulo': u'¿Su institución o usted han presentado propuestas de acciones de prevención de VBG?'}, 
        name="presenta_func"),
    url(r'^lideres/negocia-propuestas/$', 
        'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'lideres', 'model': 'calidadatencion', 'options': ['si', 'no'], 'tipo_choice': 'si_no', 'field': 'propuesta2', 'titulo': u'¿Ha negociado propuestas de acciones de prevención de VBG?'}, 
        name="negocia_lideres"),
    url(r'^funcionarios/negocia-propuestas/$', 
        'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'funcionarios', 'model': 'IncidenciaPoliticaFuncionario', 'options': ['si', 'no'], 'tipo_choice': 'simple', 'field': 'ud_negociado', 'titulo': u'¿Ud ha negociado con las mujeres de este municipio alguna propuesta que planteaba mejorar los servicios que Uds brindan?'}, 
        name="negocia_func"),                         
    url(r'^(?P<tipo>[-\w]+)/vbg-afecta-mujeres/$', 'trocaire.encuesta.views.generic_pie', 
        {'model': 'efectovbg', 'options': ['si', 'no'], 'tipo_choice': 'si_no', 'field': 'afecta_mujeres', 'titulo': u'¿Cree Ud que la VBG afecta a las mujeres, la familia y a la comunidad?'}, 
        name="vbg_afecta_mujeres"),
                       
    url(r'^funcionarios/recibido-capacitacion/$', 'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'funcionarios', 'model': 'accesoinformacion', 'options': ['si', 'no'], 'tipo_choice': 'simple', 'field': 'recibe_capacitacion', 
         'titulo': u'¿Los funcionarios de la institución donde usted trabaja han recibido capacitación relacionada con la VBG?'}),
                       
    url(r'^funcionarios/frecuencia-capacitacion/$', 'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'funcionarios', 'model': 'accesoinformacion', 'options': FRECUENCIA_CAPAC, 'tipo_choice': 'tupla', 'field': 'frecuencia', 
         'titulo': u'¿Con que frecuencia han recibido estas capacitaciones?'}),
                       
    url(r'^(?P<tipo>[-\w]+)/quienes-capacitan/$', 'trocaire.encuesta.views.generic_view', 
        {'model': 'accesoinformacion', 'options': 'BrindanCapacitacion', 'output': 'model', 'field': 'quien_brinda', 'titulo': u'¿Quienes les brindan estas capacitaciones?'}),
    
    url(r'^(?P<tipo>[-\w]+)/mencione-leyes/$', 'trocaire.encuesta.views.generic_lista', 
        {'model': 'conocimientoley', 'field': 'mencione', 'titulo': u'¿Mencione el nombre de la ley que penaliza la Violencia contra las mujeres?'}),
    #---------------------lideres-------------------------------------    
    
    (r'^(?P<tipo>[-\w]+)/tipo-propuesta/$', 'trocaire.encuesta.views.tipo_propuesta_presentada'),
    (r'^(?P<tipo>[-\w]+)/tipo-propuesta-negociada/$', 'trocaire.encuesta.views.tipo_propuesta_negociada'),
    
    (r'^lideres/$', direct_to_template, {'template': 'monitoreo/lideres.html'}),
    (r'^lideres/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_vista_lideres'),      
    
    (r'^funcionarios/$', direct_to_template, {'template': 'monitoreo/funcionarios.html'}),
    (r'^funcionarios/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_view_funcionario'),    
    
    (r'^(?P<tipo>[-\w]+)/$', 'trocaire.mujeres_hombres.views.index'),
    (r'^(?P<tipo>[-\w]+)/(?P<vista>[-\w]+)/$', 'trocaire.mujeres_hombres.views._get_view'),
)


