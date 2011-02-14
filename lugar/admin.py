from django.contrib import admin
from models import *

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'id']
    list_filter = ['pais']
    prepopulated_fields = {"slug": ("nombre", )}
    search_fields = ['nombre']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'departamento', 'id']
    list_filter = ['departamento',]    
    search_fields = ['nombre']
    prepopulated_fields = {"slug": ("nombre", )}

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Pais)
#admin.site.register(Comunidad, ComunidadAdmin)
#admin.site.register(Microcuenca, MicrocuencaAdmin)




