from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^consultar/$', 'trocaire.encuesta.views.consultar'),
    
    (r'^mujeres/$', direct_to_template, {'template': 'monitoreo/mujeres-hombres.html'}),

    (r'^lideres/$', direct_to_template, {'template': 'monitoreo/lideres.html'}),
    (r'^lideres/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_vista_lideres'),
    
    (r'^funcionarios/$', direct_to_template, {'template': 'monitoreo/funcionarios.html'}),
    (r'^funcionarios/(?P<vista>[-\w]+)/$', 'trocaire.encuesta.views._get_view_funcionario'),    
    
    (r'^(?P<tipo>[-\w]+)/(?P<vista>[-\w]+)/$', 'trocaire.mujeres_hombres.views._get_view'),
)


