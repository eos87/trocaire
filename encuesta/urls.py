# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from trocaire.lugar.models import Comunidad
from models import *

urlpatterns = patterns('',
    (r'^consultar/$', 'trocaire.encuesta.views.consultar'),

    url(r'^(?P<tipo>[-\w]+)/vbg-resolverse-con/$', 'trocaire.encuesta.views.generic_view', 
        {'model': 'asuntopublicovbg', 'options': 'resolvervbg', 'output': 'model', 'field': 'resolverse_con', 
         'titulo': u'¿Considera que la VBG es un asunto que debe ser resuelto con la participación de?', 'checkvalues': 3}),
                       
    url(r'^(?P<tipo>[-\w]+)/como-afecta-vbg/$', 'trocaire.encuesta.views.generic_view', 
        {'model': 'efectovbg', 'options': 'comoafecta', 'output': 'model', 'field': 'como_afecta', 
         'titulo': u'¿Cómo la VBG afecta a las mujeres, las familias y a las comunidades?', 'checkvalues': 3}),    
                                          
    url(r'^(?P<tipo>[-\w]+)/negociacion-exitosa-func/$', 'trocaire.encuesta.views.generic_view', 
        {'model': 'comunicacionasertiva', 'options': 'NegociacionExitosa', 'output': 'model', 'field': 'negociacion_exitosa', 
         'titulo': u'¿Qué se debe hacer para que una negociación de pareja sea exitosa?'}),                           
    
    #------------------ ha presentado y ha negociado propuestas ---------------------    
    url(r'^lideres/presenta-propuestas/$', 'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'lideres', 'model': 'calidadatencion', 'options': ['si', 'no'], 'tipo_choice': 'si_no', 'field': 'propuesta', 'titulo': u'¿Ha presentado propuestas de acciones de prevención de VBG?'}),
    
    url(r'^funcionarios/presenta-propuestas/$', 'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'funcionarios', 'model': 'IncidenciaPoliticaFuncionario', 'options': ['si', 'no'], 'tipo_choice': 'simple', 'field': 'ha_recibido', 'titulo': u'¿Su institución o usted han presentado propuestas de acciones de prevención de VBG?'}),
    
    url(r'^lideres/negocia-propuestas/$', 'trocaire.encuesta.views.generic_pie', 
        {'tipo': 'lideres', 'model': 'calidadatencion', 'options': ['si', 'no'], 'tipo_choice': 'si_no', 'field': 'propuesta2', 'titulo': u'¿Ha negociado propuestas de acciones de prevención de VBG?'}, 
        name="negocia_lideres"),
                       
    url(r'^funcionarios/negocia-propuestas/$', 'trocaire.encuesta.views.generic_pie', 
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
    
    url(r'^(?P<tipo>[-\w]+)/mencione-ley/$', 'trocaire.encuesta.views.generic_lista', 
        {'model': 'conocimientoley', 'field': 'mencione', 'titulo': u'¿Mencione el nombre de la ley que penaliza la Violencia contra las mujeres?'}),
    
    url(r'^(?P<tipo>[-\w]+)/acciones-prevenir/$', 'trocaire.encuesta.views.generic_lista', 
        {'model': 'AccionVBGLider', 'field': 'porque_no', 'titulo': u'¿Por qué no han realizado acciones dirigidas a prevenir la VBG?'}),
    
    #-------------------- salidas de lideres y funcionarios con generica hombres mujeres -----------------
    url(r'^lideres/estudia-actualmente-2/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'lideres', 'modelo': 'InformacionSocioEconomicaLider', 'options': SI_NO_SIMPLE, 'field': 'estudia', 'titulo': u'¿Estudia actualmente?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True}),    
    url(r'^funcionarios/estudia-actualmente-2/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'funcionarios', 'modelo': 'InformacionSocioEconomicaFuncionario', 'options': SI_NO_SIMPLE, 'field': 'estudia', 'titulo': u'¿Estudia actualmente?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True}),
    url(r'^lideres/nivel-educativo/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'lideres', 'modelo': 'InformacionSocioEconomicaLider', 'options': NIVEL_EDUCATIVO, 'field': 'nivel_educativo', 'titulo': u'¿Cuál es su nivel educativo más alto?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True}),
    url(r'^funcionarios/nivel-educativo/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'funcionarios', 'modelo': 'InformacionSocioEconomicaFuncionario', 'options': NIVEL_EDUCATIVO, 'field': 'nivel_educativo', 'titulo': u'¿Cuál es su nivel educativo más alto?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True}),
    url(r'^lideres/trabaja-fuera/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'lideres', 'modelo': 'InformacionSocioEconomicaLider', 'options': SI_NO_SIMPLE, 'field': 'trabaja_fuera', 'titulo': u'Trabaja usted fuera del hogar?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True}),                                                  
    url(r'^lideres/donde-trabaja/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'lideres', 'modelo': 'InformacionSocioEconomicaLider', 'options': LugarDeTrabajo.objects.all(), 'field': 'donde_trabaja', 'titulo': u'¿Donde trabaja?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True, 'checkcero': True}),
    url(r'^funcionarios/comunidad-mujeres/$', 'trocaire.mujeres_hombres.views.generic_view_hm', 
        {'tipo': 'funcionarios', 'modelo': 'IncidenciaPoliticaFuncionario', 'options': Comunidad.objects.all(), 'field': 'que_comunidades', 'titulo': u'¿De que comunidades eran las mujeres que presentaron las propuestas?', 
         'template_name': 'monitoreo/lideres/generica_lideres_pie.html', 'nocheck': True, 'nografo': True}),
        
    #----------------- fin salidas genericas --------------------
    
    url(r'^(?P<tipo>[-\w]+)/tipo-propuesta/$', 'trocaire.encuesta.views.tipo_propuesta_presentada'),
    url(r'^(?P<tipo>[-\w]+)/tipo-propuesta-negociada/$', 'trocaire.encuesta.views.tipo_propuesta_negociada'),
    
    url(r'^(?P<tipo>[-\w]+)/calidad-servicios-1/$', 'trocaire.encuesta.views.calidad_servicios'),
    url(r'^(?P<tipo>[-\w]+)/solucion-conflicto/$', 'trocaire.encuesta.views.solucion_conflicto'),
    
    url(r'^lideres/$', direct_to_template, {'template': 'monitoreo/lideres.html'}),
    url(r'^lideres/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_vista_lideres'),      
    
    url(r'^funcionarios/$', direct_to_template, {'template': 'monitoreo/funcionarios.html'}),
    url(r'^funcionarios/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_view_funcionario'),
    
    url(r'^(?P<tipo>[-\w]+)/', include('trocaire.mujeres_hombres.urls')),
)


