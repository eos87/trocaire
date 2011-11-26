# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import ViewDoesNotExist
from django.shortcuts import render_to_response, Http404
from django.template import RequestContext
from trocaire.encuesta.models import *
from trocaire.lugar.models import *
from trocaire.utils import _query_set_filtrado
from trocaire.utils import convertir_grafico
from trocaire.utils import get_content_type
from trocaire.utils import get_list_with_total
from trocaire.utils import get_prom_dead_list
from trocaire.utils import get_prom_dead_list2
from trocaire.utils import get_prom_dead_list3
from trocaire.utils import get_total


def index(request, tipo):
    if tipo == 'mujeres':
        return render_to_response('monitoreo/mujeres.html', {'tipo': tipo}, RequestContext(request))
    elif tipo == 'hombres':
        return render_to_response('monitoreo/hombres.html', {'tipo': tipo}, RequestContext(request))
    else:
        raise Http404    

def hablan_de(request, tipo='mujeres'):    
    titulo = "¿Cuando alguien le habla de VBG usted cree que le estan hablando de?"
    resultados = _query_set_filtrado(request, tipo=tipo)
    tabla = {}
    opciones = HablanDe.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]       

        for opcion in opciones:
            query = ConceptoViolencia.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, hablande=opcion, respuesta='si')
            tabla[opcion].append(query.count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) < 15:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def expresion_vbg(request, tipo):
    """Vista sobre: De que manera cree usted que se expresa la VBG"""
    titulo = '¿De que manera cree usted que se expresa la VBG?'
    resultados = _query_set_filtrado(request, tipo=tipo)
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']
    for field in campos:
        tabla[field.verbose_name] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def comportamiento(request, tipo):
    """Como deben comportarse hombres y mujeres"""
    from trocaire.encuesta.models import CREENCIAS_VBG_RESP
    resultados = _query_set_filtrado(request, tipo=tipo)
    tabla = {}
    campos = [field for field in Creencia._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            for op in CREENCIAS_VBG_RESP:
                tabla[field.verbose_name][key].append(Creencia.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: op[0]}).count())
    
    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)

    return render_to_response("monitoreo/comportamiento.html", RequestContext(request, locals()))

def hombres_violencia_mujeres(request, tipo):    
    titulo = '¿Para usted los hombres ejercen violencia hacia las mujeres porque?'
    resultados = _query_set_filtrado(request, tipo=tipo)
    tabla = {}
    campos = [field for field in JustificacionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(JustificacionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)

    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def hombres_vbg(request, tipo):    
    titulo = '¿Conoce usted si en su comunidad existen hombres que ejercen VBG?'
    resultados = _query_set_filtrado(request, tipo=tipo)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, conoce_hombres=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def mujeres_vbg(request, tipo):    
    titulo = '¿Conoce usted si en su comunidad existen mujeres que han vivido VBG?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, conoce_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def vbg_resolver_con(request, tipo):    
    titulo = u'¿Considera que la VBG es un asunto que debe ser resuelto con la participación de?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = ResolverVBG.objects.all()
    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in opciones:
            tabla[op].append(AsuntoPublicoVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, resolverse_con=op).count())
            
    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():        
        if checkvalue(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def afeccion_vbg(request, tipo):    
    titulo = u'¿Cree usted que la VBG afecta a las mujeres, la familia y la comunidad?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(EfectoVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, afecta_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)

    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def como_afecta(request, tipo):
    titulo = u'¿Como afecta la VBG a las mujeres, comunidad y la familia?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = ComoAfecta.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(EfectoVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, como_afecta=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def conoce_leyes(request, tipo):
    titulo = u'¿Sabe usted si en existe alguna ley que penaliza la violencia contra las mujeres?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}

    for op in SI_NO_RESPONDE:
        tabla[op[1]] = []
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in SI_NO_RESPONDE:
            tabla[op[1]].append(ConocimientoLey.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, existe_ley=op[0]).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def mencione_leyes(request, tipo):
    titulo = u'Mencione la ley que penaliza la VBG contra las mujeres'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    totales = get_total(resultados)
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        tabla[key] = list(set(ConocimientoLey.objects.filter(content_type=get_content_type(tipo), object_id__in=lista).values_list('mencione')))
        
    return render_to_response("monitoreo/lista_leyes.html", RequestContext(request, locals()))

def prohibido_por_ley(request, tipo):
    """Acciones prohibidas por la ley"""
    from trocaire.encuesta.models import SI_NO_RESPONDE

    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    campos = [field for field in ConocimientoLey._meta.fields if field.get_internal_type() == 'IntegerField' and not (field.name == 'existe_ley' or field.name == 'object_id')]
    
    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
                    
            tabla[field.verbose_name][key] = []            

            for op in SI_NO_RESPONDE:                
                tabla[field.verbose_name][key].append(ConocimientoLey.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: op[0]}).count())
                
    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)
    return render_to_response("monitoreo/prohibido_por_ley.html", RequestContext(request, locals()))

def hombres_violentos(request, tipo):
    titulo = "¿Cree usted que los hombres son violentos debido a?"
    resultados = _query_set_filtrado(request, tipo=tipo)
    tabla = {}
    campos = [field for field in CausaVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(CausaVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def ayuda_mujer_violencia(request, tipo):    
    titulo = u'¿En el último año ha ayudado usted a alguna mujer que ha vivido VBG?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in ['si', 'no']:
            tabla[op.title()].append(AccionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ha_ayudado=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def que_hace_ante_vbg(request, tipo):
    """Que hace usted cuando existe una situación de VBG"""
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    campos = [field for field in AccionVBG._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    opciones = [1, 2, 3, 4, 5, 6]

    for field in campos:        
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = {}            
            
            for op in opciones:
                tabla[field.verbose_name][key][op] = AccionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: op-1}).count()
    totales = get_total(resultados)
    
    #---------------Inicia transformacion para grafico ------------------------
    grafico = {}
    for key, value in tabla.items():
        grafico[key] = {}
        for i in range(1, 5):
            grafico[key][i] = obtener_indice(tabla[key][i])   
            
    return render_to_response("monitoreo/que_hace_ante_vbg.html", RequestContext(request, locals()))

#---- funcion para multiplicar la llave por su valor
calc_llave_valor = lambda x: x[0]*x[1]

def obtener_indice(dicc):    
    aux = 0        
    for valor in dicc.items():
        aux += calc_llave_valor(valor)    
    #obtener y retornar total de los values del dicc
    total = float(sum(dicc.values()))
    if total == 0:
        return 0
    else:
        return round(aux/total, 1)
    

def donde_buscar_ayuda(request, tipo):
    titulo = '¿Donde debe buscar ayuda una mujer que vive VBG?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = BuscarAyuda.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in opciones:
            tabla[op].append(AccionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, donde_buscar=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def que_debe_hacer(request, tipo):    
    titulo = "¿Si un hombre le pega a su pareja que acciones deberia de tomar?"
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = QueDebeHacer.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccionVBG.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, accion_tomar=op).count())

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)

    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def que_acciones_realizar(request, tipo):
    titulo = "¿Cuando una mujer vive VBG cuales acciones deberia realizar?"
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = Decision.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in opciones:
            tabla[op].append(TomaDecision.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, decision=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def participacion_en_espacios(request, tipo):
    titulo = u"¿En que organización o espacios comunitarios te encuentras integrada/o actualmente?"
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = Espacio.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(ParticipacionPublica.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, espacio=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def motivo_participacion(request, tipo):
    titulo = u'¿Qué le motiva a participar en esta organización?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = MotivoParticipacion.objects.all()
    
    for op in opciones:
        tabla[op] = []
        
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(ParticipacionPublica.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, motivo=op).count())
    
    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]
    
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def ha_vivido_vbg(request, tipo):
    titulo = u'¿Considera usted que alguna vez ha vivido VBG?'
    resultados = _query_set_filtrado(request, 'mujeres')
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(PrevalenciaVBG.objects.filter(content_type=get_content_type('mujeres'), object_id__in=lista, ha_vivido_vbg=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def tipo_vbg_vivido(request, tipo):
    titulo = u"¿Qué tipo de VBG ha vivido?"
    resultados = _query_set_filtrado(request, 'mujeres')
    tabla = {}
    opciones = TipoVBG.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
                
        for op in opciones:
            tabla[op].append(PrevalenciaVBG.objects.filter(content_type=get_content_type('mujeres'), object_id__in=lista, que_tipo=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def ha_ejercido_vbg(request, tipo):
    titulo = u'Considera usted que ejercido VBG contra una mujer el ultimo año?'
    resultados = _query_set_filtrado(request, 'hombres')
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(PrevalenciaVBGHombre.objects.filter(content_type=get_content_type('hombres'), object_id__in=lista, ha_vivido_vbg=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def tipo_vbg_ejercido(request, tipo):
    titulo = u"¿Qué tipo de VBG ha ejercido?"
    resultados = _query_set_filtrado(request, 'hombres')
    tabla = {}
    opciones = TipoVBG.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
       
        for op in opciones:
            tabla[op].append(PrevalenciaVBGHombre.objects.filter(content_type=get_content_type('hombres'), object_id__in=lista, que_tipo=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def frecuencia(request, tipo):
    from trocaire.encuesta.models import FRECUENCIA2, FRECUENCIA    
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    
    if tipo == 'mujeres':
        opciones = FRECUENCIA
        titulo = u'¿Con que frecuencia ha vivido VBG este último año?'
    elif tipo == 'hombres':
        titulo = u'¿Con que frecuencia ha ejercido VBG este último año?'
        opciones = FRECUENCIA2
        
    for op in opciones:
        tabla[op[1]] = []
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
       
        for op in opciones:
            if tipo == 'mujeres':
                tabla[op[1]].append(PrevalenciaVBG.objects.filter(content_type=get_content_type(tipo), 
                                                                    object_id__in=lista, 
                                                                    frecuencia=op[0]).count())
            elif tipo == 'hombres':
                tabla[op[1]].append(PrevalenciaVBGHombre.objects.filter(content_type=get_content_type(tipo), 
                                                                    object_id__in=lista, 
                                                                    frecuencia=op[0]).count())    
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))
        
def parentesco_ha_ejercido(request, tipo):
    titulo = u'¿Qué parentesco tiene con la persona que ha ejercido VBG?'
    resultados = _query_set_filtrado(request, 'hombres')
    tabla = {}
    opciones = Quien2.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(PrevalenciaVBGHombre.objects.filter(content_type=get_content_type('hombres'), 
                                                                 object_id__in=lista, 
                                                                 quien=op).count())

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def actividades_hogar(request, tipo):
    """Cuales de las siguientes actividades realiza usted en su hogar"""
    from trocaire.encuesta.models import HOGAR
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    campos = [field for field in Corresponsabilidad._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            for op in HOGAR:
                tabla[field.verbose_name][key].append(Corresponsabilidad.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list2(tabla, totales)
    return render_to_response("monitoreo/actividades_hogar.html", RequestContext(request, locals()))

def solucion_problema(request, tipo):
    titulo = u'¿Que se debe hacer para que la solucion a un conflicto entre la pareja sea exitoso?'
    from trocaire.encuesta.models import DES_AC
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    campos = [field for field in ComunicacionAsertiva._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']
    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []            
            for op in DES_AC:
                tabla[field.verbose_name][key].append(ComunicacionAsertiva.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list3(tabla, totales)

    return render_to_response("monitoreo/solucion_problema.html", RequestContext(request, locals()))

def negociacion_pareja(request, tipo):
    """Que se debe hacer para que una negociacion de pareja sea exitosa"""
    titulo = u'¿Que se debe hacer para que una negociacion de pareja sea exitosa?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = NegociacionExitosa.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(ComunicacionAsertiva.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, negociacion_exitosa=op).count())

    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def mujeres_representan(request, tipo):    
    titulo = u'¿En su comunidad existen mujeres que representan a otras mujeres?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in ['si', 'no']:
            tabla[op.title()].append(IncidenciaPolitica.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, existen_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def satisfaccion(request, tipo):
    titulo = u'¿Qué tan satisfechas están las mujeres con quienes las representan?'
    from trocaire.encuesta.models import SATISFECHAS    
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = SATISFECHAS
        
    for op in opciones:
        tabla[op[1]] = []
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
       
        for op in opciones:            
            tabla[op[1]].append(IncidenciaPolitica.objects.filter(content_type=get_content_type(tipo), 
                                                                    object_id__in=lista, 
                                                                    satisfecha=op[0]).count())    
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def calidad_servicios(request, tipo):
    titulo = u'¿Cómo valora Ud los servicios que las intituciones ofrecen a las mujeres que viven VBG?'
    from trocaire.encuesta.models import SERVICIOS
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = SERVICIOS
        
    for op in opciones:
        tabla[op[1]] = []
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
       
        for op in opciones:            
            tabla[op[1]].append(CalidadAtencion.objects.filter(content_type=get_content_type(tipo), 
                                                                    object_id__in=lista,
                                                                    valor_servicio=op[0]).count())    
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def nivel_educativo(request, tipo):
    from trocaire.encuesta.models import NIVEL_EDUCATIVO
    titulo = u'¿Cuál es su nivel educativo más alto?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    
    opciones = NIVEL_EDUCATIVO

    for op in opciones:
        tabla[op[1]] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op[1]].append(InformacionSocioEconomica.objects.filter(content_type=get_content_type(tipo), 
                                                                      object_id__in=lista, 
                                                                      nivel_educativo=op[0]).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def viven_con_pareja(request, tipo):
    from trocaire.encuesta.models import SI_NO
    titulo = u'¿Actualmente tiene esposo/a o compañero/a?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}

    for op in SI_NO:
        tabla[op[1]] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in SI_NO:
            tabla[op[1]].append(ComposicionHogar.objects.filter(content_type=get_content_type(tipo), object_id__in=lista, tiene_pareja=op[0]).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def trabaja_fuera(request, tipo):
    titulo = u'¿Trabaja usted fuera del hogar?'
    resultados = _query_set_filtrado(request, tipo)
    tabla ={}
    
    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        
        for op in ['si', 'no']:
            tabla[op.title()].append(InformacionSocioEconomica.objects.filter(content_type=get_content_type(tipo), 
                                                                              object_id__in=lista, trabaja_fuera=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def aporte_ingresos(request, tipo):
    titulo = u'¿Quién a quienes aportan ingresos al hogar?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    
    opciones = Aporta.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(InformacionSocioEconomica.objects.filter(content_type=get_content_type(tipo), 
                                                                      object_id__in=lista, 
                                                                      aportan=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def mencione_recursos(request, tipo):
    titulo = u'¿Mencione los recursos de los que es dueña/o?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = Recurso.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccesoControlRecurso.objects.filter(content_type=get_content_type(tipo), 
                                                                      object_id__in=lista, 
                                                                      recursos=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def decide_recursos(request, tipo):
    titulo = u'¿Mencione los recursos sobre los cuales ud decide?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = Recurso.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccesoControlRecurso.objects.filter(content_type=get_content_type(tipo), 
                                                                      object_id__in=lista, 
                                                                      recursos_decide=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def que_hace_dinero(request, tipo):
    from trocaire.encuesta.models import QUE_HACE_DINERO
    titulo = u'¿Que hace usted con el dinero que gana?'
    resultados = _query_set_filtrado(request, tipo)
    tabla = {}
    opciones = QUE_HACE_DINERO

    for op in opciones:
        tabla[op[1]] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op[1]].append(InformacionSocioEconomica.objects.filter(content_type=get_content_type(tipo), 
                                                                      object_id__in=lista, 
                                                                      hace_dinero=op[0]).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def persona_ejercido(request, tipo):
    titulo = u'¿Quién es la persona que ha ejercido VBG sobre usted?'
    resultados = _query_set_filtrado(request, 'mujeres')
    tabla = {}
    
    opciones = Quien.objects.all()
    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(PrevalenciaVBG.objects.filter(content_type=get_content_type('mujeres'), 
                                                                      object_id__in=lista, 
                                                                      quien=op).count())
    totales = get_total(resultados)
    tabla = get_list_with_total(tabla, totales)    
    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))    

#obtener la vista adecuada para los indicadores
def _get_view(request, tipo, vista):
    if vista in VALID_VIEWS:
        if tipo == 'mujeres' or tipo == 'hombres':
            return VALID_VIEWS[vista](request, tipo)
        else:
            raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'hablan-de': hablan_de,
    'expresion-vbg': expresion_vbg,
    'hombres-que-ejercen-vbg': hombres_vbg,
    'mujeres-viven-vbg': mujeres_vbg,
    'vbg-se-resuelve-con': vbg_resolver_con,
    'afeccion-vbg': afeccion_vbg,
    'como-afecta': como_afecta,
    'conoce-leyes': conoce_leyes,
    'mencione-leyes': mencione_leyes,
    'prohibido-por-ley': prohibido_por_ley,
    'hombres-violentos-por': hombres_violentos,
    'hombres-violencia-mujeres': hombres_violencia_mujeres,
    'comportamiento': comportamiento,
    'ayuda-mujer-violencia': ayuda_mujer_violencia,
    'que-hace-ante-vbg': que_hace_ante_vbg,
    'donde-buscar-ayuda': donde_buscar_ayuda,
    'que-debe-hacer': que_debe_hacer,
    'que-acciones-realizar': que_acciones_realizar,
    'participacion-en-espacios': participacion_en_espacios,
    'motivo-participacion': motivo_participacion,
    'ha-vivido-vbg': ha_vivido_vbg,
    'tipo-vbg-vivido': tipo_vbg_vivido,
    'ha-ejercido-vbg': ha_ejercido_vbg,
    'tipo-vbg-ejercido': tipo_vbg_ejercido,
    'frecuencia-ejercido': frecuencia,
    'frecuencia-vivido': frecuencia,
    'actividades-hogar': actividades_hogar,
    'solucion-problema': solucion_problema,
    'negociacion-pareja': negociacion_pareja,
    'mujeres-representan': mujeres_representan,
    'nivel-educativo': nivel_educativo,
    'viven-con-pareja': viven_con_pareja,
    'trabaja-fuera': trabaja_fuera,
    'aporte-ingresos': aporte_ingresos,
    'mencione-recursos': mencione_recursos,
    'decide-recursos': decide_recursos,
    'que-hace-dinero': que_hace_dinero,
    'persona-ejercido': persona_ejercido,
    'parentesco-ha-ejercido': parentesco_ha_ejercido,
    'satisfaccion': satisfaccion,
    'calidad-servicios': calidad_servicios,
    }
