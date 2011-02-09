# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.forms import CheckboxSelectMultiple
from models import *
from trocaire.lugar.models import *

class ComposicionHogarInline(generic.GenericStackedInline):
    model = ComposicionHogar
    max_num = 1
    fieldsets = [
        (None, {'fields': [('tiene_pareja', 'vive_con')]}),
        (u'Habitantes del hogar', {'fields': ['cuantos_viven', ('entre0y6', 'entre7y17', 'entre18ymas'), 'tiene_hijos', 'cuantos_hijos']}),
        (u'7. Qué edad tienen los hijos e hijas que viven con usted', {
            'classes': ('clase_propia',),
            'description': u'<b>Número de niños entre 0 y 6 años</b>',
            'fields': [('hijos0y6_mujeres', 'hijos0y6_hombres')]
        }),
        (None, {
            'description': u'<b>Número de niños entre 7 y 17 años</b>',            
            'fields': [('hijos7y17_mujeres', 'hijos7y17_hombres'),]
        }),
        (None, {
            'description': u'<b>Número de personas entre 18 y más años</b>',
            'fields': [('hijos18ymas_mujeres', 'hijos18ymas_hombres'),]
        }),
    ]

class InfoSocioEconomicaInline(generic.GenericStackedInline):    
    filter_horizontal = ['donde_trabaja', 'aportan']
    model = InformacionSocioEconomica
    max_num = 1
    verbose_name = u'Información SocioEconómica'
    verbose_name_plural = u'V. Información SocioEconómica'

class AccesoControlRecursoInline(generic.GenericStackedInline):
    model = AccesoControlRecurso    
    max_num = 1

class ConceptoViolenciaInline(generic.GenericTabularInline):
    model = ConceptoViolencia
    extra = 1
    radio_fields = {
        'respuesta': admin.HORIZONTAL,
    }

class ExpresionVBGInline(generic.GenericTabularInline):
    model = ExpresionVBG
    extra = 1
    radio_fields = {
        'respuesta': admin.HORIZONTAL,
    }

class CreenciaInline(generic.GenericTabularInline):
    model = Creencia
    extra = 1

    radio_fields = {
        'respuesta': admin.HORIZONTAL,
    }

class JustificacionVBGInline(generic.GenericTabularInline):
    model = JustificacionVBG
    extra = 1

class CausaVBGInline(generic.GenericTabularInline):
    model = CausaVBG
    extra = 1

class SituacionVBGInline(generic.GenericTabularInline):
    model = SituacionVBG
    max_num = 1

class AccionVBGInline(generic.GenericStackedInline):
    model = AccionVBG
    pregunta = '¿Qié hace Ud cuando existe una situación de VBG en su comunidad?'
    fieldsets = [
        (None, {'fields': ['ha_ayudado']}),
        (pregunta, {'fields': ['se_acerca', 'invita_actividad', 'no_hace_nada', 'no_hace_problema', 'busca_alternativa', 'no_sabe']}),
        (None, {'fields': ['donde_buscar', 'accion_tomar']})
    ]
    radio_fields = {
        'se_acerca': admin.HORIZONTAL,
        'invita_actividad': admin.HORIZONTAL,
        'no_hace_nada': admin.HORIZONTAL,
        'no_hace_problema': admin.HORIZONTAL,
        'busca_alternativa': admin.HORIZONTAL,
        'no_sabe': admin.HORIZONTAL
    }
    filter_horizontal = ['donde_buscar', 'accion_tomar']
    max_num = 1

class PrevalenciaVBGInline(generic.GenericStackedInline):
    verbose_name_plural = 'Prevalencia de la Violencia Basada en Género'
    verbose_name = 'Prevalencia de la VBG'
    model = PrevalenciaVBG
    filter_horizontal = ['quien',]
    max_num = 1

admin.site.register(TipoVBG)

class AsuntoPublicoVBGInline(generic.GenericStackedInline):
    model = AsuntoPublicoVBG
    filter_horizontal = ['resolverse_con',]
    max_num = 1

class EfectoVBGInline(generic.GenericStackedInline):
    model = EfectoVBG
    filter_horizontal = ['como_afecta',]
    max_num = 1

class ConocimientoLeyInline(generic.GenericStackedInline):
    model = ConocimientoLey
    pregunta = 'Sabe Ud cuales de las siguientes acciones son prohibidas por la ley'
    fieldsets = [
        (None, {'fields': ['existe_ley', 'mencione']}),
        (pregunta, {'fields': [('padre_golpea', 'maestro_castiga', 'maestro_relacion'), ('joven_case', 'joven_relacion', 'patron_acoso'), ('lider_religioso', 'adulto_relacion', 'adulto_dinero')]}),
    ]
    max_num = 1

class TomaDecisionInline(generic.GenericStackedInline):
    model = TomaDecision
    filter_horizontal = ['decision',]
    max_num = 1

class ParticipacionPublicaInline(generic.GenericStackedInline):
    model = ParticipacionPublica
    filter_horizontal = ['espacio', 'motivo']
    max_num = 1

class IncidenciaPoliticaInline(generic.GenericTabularInline):
    model = IncidenciaPolitica
    max_num = 1

class CalidadAtencionInline(generic.GenericStackedInline):
    model = CalidadAtencion
    max_num = 1

class CorresponsabilidadInline(generic.GenericStackedInline):
    model = Corresponsabilidad
    max_num = 1
    pregunta = '¿Cuáles de las siguientes actividades realiza Ud en su hogar?'
    fieldsets = [
        (pregunta, {'fields': ['lavar', 'plancar', 'limpiar',
                                'jalar_agua', 'cuidar_ninos', 'hacer_mandados',
                                'llevar_lena', 'lavar_trastes', 'arreglar_cama',
                                'ir_reuniones', 'acompanar', 'hacer_compras',
                                'pagar_servicios', 'llevar_enfermos', 'cuidar_enfermos']}),
    ]
    radio_fields = {
        'lavar': admin.HORIZONTAL,
        'plancar': admin.HORIZONTAL,
        'limpiar': admin.HORIZONTAL,
        'jalar_agua': admin.HORIZONTAL,
        'cuidar_ninos': admin.HORIZONTAL,
        'hacer_mandados': admin.HORIZONTAL,
        'llevar_lena': admin.HORIZONTAL,
        'lavar_trastes': admin.HORIZONTAL,
        'arreglar_cama': admin.HORIZONTAL,
        'ir_reuniones': admin.HORIZONTAL,
        'acompanar': admin.HORIZONTAL,
        'hacer_compras': admin.HORIZONTAL,
        'pagar_servicios': admin.HORIZONTAL,
        'llevar_enfermos': admin.HORIZONTAL,
        'cuidar_enfermos': admin.HORIZONTAL,
    }

class ComunicacionAsertivaInline(generic.GenericStackedInline):
    model = ComunicacionAsertiva
    filter_horizontal = ['negociacion_exitosa',]
    max_num = 1
    pregunta = u'¿Qué se debe hacer para que una solución a un conflicto entre pareja sea exitoso?'

    fieldsets = [
        (pregunta, {'fields': ['identificar', 'analizar', 'identificar_prioridad', 'pido', 'actitud_pasiva']}),
        (None, {'fields': ['negociacion_exitosa',]}),
    ]

    radio_fields = {
        'identificar': admin.HORIZONTAL,
        'analizar': admin.HORIZONTAL,
        'identificar_prioridad': admin.HORIZONTAL,
        'pido': admin.HORIZONTAL,
        'actitud_pasiva': admin.HORIZONTAL,
    }

class MujeresAdmin(admin.ModelAdmin):    
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    list_display = ['contraparte', 'encuestador', 'fecha']
    #list_display_links = ['contraparte', 'encuestador', 'fecha']
    #list_editable = ['encuestador', 'fecha']    

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
        PrevalenciaVBGInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ConocimientoLeyInline,
        TomaDecisionInline,
        ParticipacionPublicaInline,
        IncidenciaPoliticaInline,
        CalidadAtencionInline,
        CorresponsabilidadInline,
        ComunicacionAsertivaInline,
        ]

admin.site.register(Mujer, MujeresAdmin)

class PrevalenciaVBGHombreInline(generic.GenericStackedInline):
    verbose_name_plural = 'Prevalencia de la Violencia Basada en Género'
    verbose_name = 'Prevalencia de la VBG'
    model = PrevalenciaVBGHombre
    filter_horizontal = ['quien',]
    max_num = 1

class HombresAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    list_display = ['contraparte', 'encuestador', 'fecha']
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
        PrevalenciaVBGHombreInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ConocimientoLeyInline,
        TomaDecisionInline,
        ParticipacionPublicaInline,
        IncidenciaPoliticaInline,
        CalidadAtencionInline,
        CorresponsabilidadInline,
        ComunicacionAsertivaInline,
        ]

admin.site.register(Hombre, HombresAdmin)

class InformacionSocioEconomicaLiderInline(generic.GenericStackedInline):
    filter_horizontal = ['donde_trabaja']
    model = InformacionSocioEconomicaLider
    max_num = 1

class AccionVBGLiderInline(generic.GenericStackedInline):
    model = AccionVBGLider
    pregunta = '¿Qué hace Ud cuando existe una situación de VBG en su comunidad?'
    fieldsets = [
        (None, {'fields': ['ha_ayudado']}),
        (pregunta, {'fields': ['se_acerca', 'invita_actividad', 'no_hace_nada', 'no_hace_problema', 'busca_alternativa', 'no_sabe']}),
        (None, {'fields': ['donde_buscar', 'accion_tomar']}),
        ('En su organización', {'fields': ['ud_previene', 'accion_prevenir', 'porque_no']})
    ]
    radio_fields = {
        'se_acerca': admin.HORIZONTAL,
        'invita_actividad': admin.HORIZONTAL,
        'no_hace_nada': admin.HORIZONTAL,
        'no_hace_problema': admin.HORIZONTAL,
        'busca_alternativa': admin.HORIZONTAL,
        'no_sabe': admin.HORIZONTAL
    }
    filter_horizontal = ['donde_buscar', 'accion_tomar', 'accion_prevenir']
    max_num = 1

class PrevalenciaVBGLiderInline(generic.GenericStackedInline):
    verbose_name_plural = 'Prevalencia de la Violencia Basada en Género'
    verbose_name = 'Prevalencia de la VBG'
    model = PrevalenciaVBGLider
    filter_horizontal = ['quien',]
    max_num = 1

class LiderAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    list_display = ['contraparte', 'encuestador', 'organizacion', 'fecha']
    inlines = [InformacionSocioEconomicaLiderInline,        
        ConceptoViolenciaInline,
        ExpresionVBGInline,
        CreenciaInline,
        JustificacionVBGInline,
        CausaVBGInline,
        SituacionVBGInline,
        AccionVBGLiderInline,
        PrevalenciaVBGLiderInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ConocimientoLeyInline,
        TomaDecisionInline,        
        IncidenciaPoliticaInline,
        CalidadAtencionInline,
        CorresponsabilidadInline,
        ComunicacionAsertivaInline,
        ]

admin.site.register(Lider, LiderAdmin)

class InformacionSocioEconomicaFuncionarioInline(generic.GenericTabularInline):
    model = InformacionSocioEconomicaFuncionario
    max_num = 1

class AccesoInformacionInline(generic.GenericTabularInline):
    model = AccesoInformacion
    max_num = 1

class RutaCriticaInline(generic.GenericStackedInline):
    model = RutaCritica
    max_num = 1
    pregunta = '¿Puede mencionar ed manera ordenada los pasos de la ruta crítica de la violencia?'
    pregunta2 = 'Puede mencionarme algunos de los diferentes intrumentos jurídicos que se utilizan en su institución en la atención a los casos de violencia'
    fieldsets = [
        (None, {'fields': ['pasos']}),
        (pregunta, {'fields': ['centro_mujeres', 'centro_salud', 'comisaria', 'juzgado', 'ministerio_publico']}),
        (pregunta2, {'fields': ['instrumentos']}),
    ]

    radio_fields = {
        'centro_mujeres': admin.HORIZONTAL,
        'centro_salud': admin.HORIZONTAL,
        'comisaria': admin.HORIZONTAL,
        'juzgado': admin.HORIZONTAL,
        'ministerio_publico': admin.HORIZONTAL,
    }

    filter_horizontal = ['instrumentos']

class AccionVBGFuncionarioInline(generic.GenericStackedInline):
    model = AccionVBGFuncionario
    filter_horizontal = ['donde_buscar', 'accion_tomar']
    max_num = 1

class RegistroDatoInline(generic.GenericStackedInline):
    model = RegistroDato
    pregunta = '¿Qué cantidad de casos de VBG han registrado?'
    fieldsets = [
        (None, {'fields': ['lleva_registro', 'cuantos']}),
        (pregunta, {'fields': [('fisica', 'sexual', 'emocional'), ('sicologica', 'otro')]}),
    ]
    max_num = 1

class CalidadAtencionFuncionarioInline(generic.GenericTabularInline):
    model = CalidadAtencionFuncionario    
    max_num = 1

class AccionMejorarAtencionInline(generic.GenericStackedInline):
    model = AccionMejorarAtencion
    filter_horizontal = ['cuales', 'recursos']
    max_num = 1

class AccionPrevVBGInline(generic.GenericStackedInline):
    model = AccionPrevVBG
    filter_horizontal = ['accion_prevenir']
    max_num = 1

class IncidenciaPoliticaFuncionarioInline(generic.GenericStackedInline):
    model = IncidenciaPoliticaFuncionario
    filter_horizontal = ['que_comunidades', 'tipo_propuestas', 'que_propuestas']    
    fields = ['ha_recibido', 'que_comunidades', 'tipo_propuestas', 'ud_negociado', 'que_propuestas']
    max_num = 1

class FuncionarioAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    list_display = ['contraparte', 'encuestador', 'institucion', 'fecha']
    inlines = [InformacionSocioEconomicaFuncionarioInline,
        ConceptoViolenciaInline,
        ExpresionVBGInline,
        CreenciaInline,
        JustificacionVBGInline,
        CausaVBGInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ComunicacionAsertivaInline,
        AccesoInformacionInline,
        ConocimientoLeyInline,
        RutaCriticaInline,
        AccionVBGFuncionarioInline,
        RegistroDatoInline,
        CalidadAtencionFuncionarioInline,
        AccionMejorarAtencionInline,
        AccionPrevVBGInline,
        IncidenciaPoliticaFuncionarioInline,
        ]

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Accion)
admin.site.register(RecursoCuentaIns)
admin.site.register(AccionPrevencion)

#temporales para agregar en el admin
admin.site.register(ViveCon)
admin.site.register(HablanDe)
admin.site.register(LugarDeTrabajo)
admin.site.register(Recurso)
admin.site.register(Comunidad)
admin.site.register(Encuestador)
admin.site.register(Contraparte)
admin.site.register(Quien)
admin.site.register(Quien2)
admin.site.register(ResolverVBG)
admin.site.register(ComoAfecta)
admin.site.register(Decision)
admin.site.register(TomaDecision)
admin.site.register(Espacio)
admin.site.register(MotivoParticipacion)
admin.site.register(SolucionConflicto)
admin.site.register(NegociacionExitosa)
admin.site.register(Aporta)
admin.site.register(BuscarAyuda)
admin.site.register(QueDebeHacer)
admin.site.register(TipoPropuesta)
admin.site.register(Organizacion)
admin.site.register(Institucion)
admin.site.register(Instrumento)