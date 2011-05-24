from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('trocaire.monitoreopf.views',
    (r'^consultar/$', 'consultarpf'),
    (r'^proposito/$', 'proposito'),
    (r'^(?P<tipo>[-\w]+)/afeccion-vbg/$', 'afeccion_vbg'),
    (r'^(?P<tipo>[-\w]+)/como-afecta/$', 'como_afecta'),
    (r'^(?P<tipo>[-\w]+)/calidad-servicios/$', 'calidad_servicios'),
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
