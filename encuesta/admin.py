# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.forms import CheckboxSelectMultiple
from models import *
from trocaire.lugar.models import *

class ComposicionHogarInline(generic.GenericTabularInline):
    """def formfield_for_manytomany(self, db_field, request=None, ** kwargs):
        
        # If it uses an intermediary model, don't show field in admin.
        #if db_field.rel.through is not None:
        #    return None

        if db_field.name in self.raw_id_fields:
            kwargs['widget'] = admin.widgets.ManyToManyRawIdWidget(db_field.rel)
            kwargs['help_text'] = ''
        elif db_field.name in (list(self.filter_vertical) + list(self.filter_horizontal)):
            kwargs['widget'] = admin.widgets.FilteredSelectMultiple(db_field.verbose_name, (db_field.name in self.filter_vertical))
        else:
            kwargs['widget'] = widgets.CheckboxSelectMultiple()
            kwargs['help_text'] = ''

        return db_field.formfield(** kwargs)"""
    
    model = ComposicionHogar
    max_num = 1

class InfoSocioEconomicaInline(generic.GenericStackedInline):    
    filter_horizontal = ['donde_trabaja', 'aportan']
    model = InformacionSocioEconomica
    max_num = 1

class AccesoControlRecursoInline(generic.GenericTabularInline):    
    model = AccesoControlRecurso    
    max_num = 1

class ConceptoViolenciaInline(generic.GenericTabularInline):
    model = ConceptoViolencia
    extra = 1

class ExpresionVBGInline(generic.GenericTabularInline):
    model = ExpresionVBG
    extra = 1

class CreenciaInline(generic.GenericTabularInline):
    model = Creencia
    extra = 1

class JustificacionVBGInline(generic.GenericTabularInline):
    model = JustificacionVBG
    extra = 1

class CausaVBGInline(generic.GenericTabularInline):
    model = CausaVBG
    extra = 1

class SituacionVBGInline(generic.GenericTabularInline):
    model = SituacionVBG
    max_num = 1

#inline especial que se incluye dentro de otro
class QueHaceUdInline(admin.TabularInline):
    model = QueHaceUd
    max_num = 1

class AccionVBGInline(generic.GenericTabularInline):
    model = AccionVBG    
    max_num = 1

class AccionVBGAdmin(admin.ModelAdmin):
    inlines = [QueHaceUdInline,]

class MujeresAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css",)
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    inlines = [ComposicionHogarInline,
        InfoSocioEconomicaInline,
        AccesoControlRecursoInline,
        ConceptoViolenciaInline,
        ExpresionVBGInline,
        CreenciaInline,
        JustificacionVBGInline,
        CausaVBGInline,
        SituacionVBGInline,
        AccionVBGInline,
        ]

admin.site.register(Mujer, MujeresAdmin)
admin.site.register(ViveCon)
admin.site.register(LugarDeTrabajo)
admin.site.register(Recurso)
