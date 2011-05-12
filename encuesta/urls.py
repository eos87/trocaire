from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('trocaire.encuesta.views',
    (r'^consultar/$', 'consultar'),
    (r'^mujeres-hombres/$', direct_to_template, {'template': 'monitoreo/mujeres-hombres.html'}),
    (r'^mujeres-hombres/(?P<vista>[-\w]+)/$', '_get_view'),
    (r'^lideres/$', direct_to_template, {'template': 'monitoreo/lideres.html'}),
    (r'^lideres/(?P<vista>[-\w]+)/$', '_get_vista_lideres'),
    (r'^funcionarios/$', direct_to_template, {'template': 'monitoreo/funcionarios.html'}),
    (r'^funcionarios/(?P<vista>[-\w]+)/$', '_get_view_funcionario'),    
)


