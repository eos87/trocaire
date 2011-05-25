from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('trocaire.monitoreopf.views',
    (r'^consultar/$', 'consultarpf'),
    (r'^proposito/$', 'proposito'),
    (r'^fin/$', 'fin'),
    (r'^(?P<tipo>[-\w]+)/afeccion-vbg/$', 'afeccion_vbg'),
    (r'^(?P<tipo>[-\w]+)/como-afecta/$', 'como_afecta'),
    (r'^(?P<tipo>[-\w]+)/calidad-servicios/$', 'calidad_servicios'),
    (r'^(?P<tipo>[-\w]+)/nivel-educativo/$', 'nivel_educativo'),
    (r'^(?P<tipo>[-\w]+)/viven-con-pareja/$', 'viven_con_pareja'),
    (r'^(?P<tipo>[-\w]+)/trabaja-fuera/$', 'trabaja_fuera'),
    (r'^(?P<tipo>[-\w]+)/aporte-ingresos/$', 'aporte_ingresos'),
    (r'^(?P<tipo>[-\w]+)/mencione-recursos/$', 'mencione_recursos'),
    (r'^(?P<tipo>[-\w]+)/decide-recursos/$', 'decide_recursos'), 
    (r'^(?P<tipo>[-\w]+)/actividades-hogar/$', 'actividades_hogar'), 
    (r'^(?P<tipo>[-\w]+)/ha-vivido-vbg/$', 'ha_vivido_vbg'),
    (r'^(?P<tipo>[-\w]+)/tipo-vbg-vivido/$', 'tipo_vbg_vivido'),  
    (r'^(?P<tipo>[-\w]+)/frecuencia/$', 'frecuencia'),  
    (r'^(?P<tipo>[-\w]+)/persona-ejercido/$', 'persona_ejercido'),
    (r'^(?P<tipo>[-\w]+)/ha-ejercido-vbg/$', 'ha_ejercido_vbg'),
    (r'^(?P<tipo>[-\w]+)/tipo-vbg-ejercido/$', 'tipo_vbg_ejercido'),
    (r'^(?P<tipo>[-\w]+)/parentesco-ha-ejercido/$', 'parentesco_ha_ejercido'),    
)

#url para lideres y funcionarios
urlpatterns += patterns('trocaire.encuesta.views',
                (r'^mujeres-vbg-comunidad/$', 'mujeres_vbg_comunidad'),
                (r'^prevenir-vbg/$', 'prevenir_vbg'),
                (r'^calidad-servicios/$', 'calidad_servicios'),
                (r'^mejorar-atencion/$', 'mejorar_atencion'),
                (r'^que-acciones/$', 'que_acciones'),
                (r'^registro-datos/$', 'registro_datos'),
                (r'^casos-registrados-por-tipo/$', 'casos_registrados_por_tipo'),                                
)
