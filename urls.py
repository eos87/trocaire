from django.conf.urls.defaults import *
from trocaire.settings import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'trocaire.views.index'),
    (r'^monitoreo/', include('trocaire.encuesta.urls')),
    (r'^monitoreopf/', include('trocaire.monitoreopf.urls')),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    (r'^admin/', include(admin.site.urls)),
	#urls lista para devolver los depas, munis via ajax
    (r'^ajax/depa/$', 'trocaire.views.get_depas'),
    (r'^ajax/muni/$', 'trocaire.views.get_munis'),
    (r'^ajax/data/$', 'trocaire.views.__get_data'),
    (r'^ajax/depas-groups/$', 'trocaire.views.get_group_depas'),
    (r'^ajax/orgs/$', 'trocaire.views.get_orgs'),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
                           )
