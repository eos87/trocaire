from django.conf.urls.defaults import *
from trocaire.settings import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^trocaire/', include('trocaire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^ajax/depa/$', 'trocaire.views.get_depas'),
    (r'^ajax/muni/$', 'trocaire.views.get_munis'),
    (r'^ajax/data/$', 'trocaire.views.__get_data'),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
                           )