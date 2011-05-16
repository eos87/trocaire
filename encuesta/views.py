# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import ViewDoesNotExist
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ConsultarForm
from models import *
from trocaire.lugar.models import *

#funcion lambda que calcula los totales a partir de la consulta filtrada
get_total = lambda x: [v.count() for k, v in x.items()]

def consultar(request):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            request.session['year'] = form.cleaned_data['year']
            request.session['nivel_educativo'] = form.cleaned_data['nivel_educativo']
            request.session['iglesia'] = form.cleaned_data['iglesia']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['centinela'] = 1
            centinela = 1
    else:
        form = ConsultarForm()
        centinela = 0

    return render_to_response("monitoreo/consultar.html", RequestContext(request, locals()))

#funcion destinada a devolver las encuestas en rangos de edad
def _query_set_filtrado(request, tipo='mujer'):
    params = {}
    #validar y crear los filtros de la consulta
    if request.session['year']:
        params['fecha__year'] = request.session['year']

    if request.session['nivel_educativo']:
        params['informacion_socio__in'] = InformacionSocioEconomica.objects.filter(nivel_educativo=request.session['nivel_educativo'])

    if request.session['iglesia'] and request.session['iglesia'] == 1:
        params['asiste_iglesia'] = True

    if request.session['pais']:
        if request.session['departamento']:
            if request.session['organizacion']:
                params['contraparte__in'] = request.session['organizacion']
            if request.session['municipio']:
                params['municipio__in'] = request.session['municipio']
            if not request.session['organizacion'] and not request.session['municipio']:
                params['municipio__in'] = Municipio.objects.filter(departamento__in=request.session['departamento'])
        else:
            params['municipio__in'] = Municipio.objects.filter(departamento__in=Departamento.objects.filter(pais__in=request.session['pais']))

    dicc = {}
    if tipo == 'mujer':
        dicc[1] = Mujer.objects.filter(edad__range=(10, 13), ** params)
        dicc[2] = Mujer.objects.filter(edad__range=(14, 17), ** params)
        dicc[3] = Mujer.objects.filter(edad__gt=18, ** params)        
        dicc[4] = Hombre.objects.filter(edad__range=(10, 13), ** params)
        dicc[5] = Hombre.objects.filter(edad__range=(14, 17), ** params)
        dicc[6] = Hombre.objects.filter(edad__gt=18, ** params)
        return dicc

    if tipo == 'especial':
        dicc[1] = Mujer.objects.filter(edad__range=(10, 13), ** params)
        dicc[2] = Mujer.objects.filter(edad__range=(14, 17), ** params)
        dicc[3] = Mujer.objects.filter(edad__gt=18, ** params)
        dicc[4] = Mujer.objects.filter(** params)
        dicc[5] = Hombre.objects.filter(edad__range=(10, 13), ** params)
        dicc[6] = Hombre.objects.filter(edad__range=(14, 17), ** params)
        dicc[7] = Hombre.objects.filter(edad__gt=18, ** params)
        dicc[8] = Hombre.objects.filter(** params)
        return dicc
    elif tipo == 'funcionario':
        dicc[1] = Funcionario.objects.filter(sexo='femenino', ** params)
        dicc[2] = Funcionario.objects.filter(sexo='masculino', ** params)
        return dicc
    elif tipo == 'lider':
        dicc[1] = Lider.objects.filter(sexo='femenino', ** params)
        dicc[2] = Lider.objects.filter(sexo='masculino', ** params)
        return dicc

def hablan_de(request):
    """Vista sobre: Cuando alguien le habla de VBG usted cree que estan hablando de:"""
    titulo = "¿Cuando alguien le habla de VBG usted cree que le estan hablando de?"
    resultados = _query_set_filtrado(request, tipo='especial')
    tabla = {}
    opciones = HablanDe.objects.all()
    
    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 5:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")

        for opcion in opciones:
            query = ConceptoViolencia.objects.filter(content_type=content, object_id__in=lista, hablande=opcion, respuesta='si')
            tabla[opcion].append(query.count())            

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():        
        if checkvalue(value) < 15:
            del tabla[key]
            
    totales = get_total(resultados)    
    tabla = get_prom_lista_con_total(tabla, totales)

    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def expresion_vbg(request):
    """Vista sobre: De que manera cree usted que se expresa la VBG"""
    titulo = '¿De que manera cree usted que se expresa la VBG?'
    resultados = _query_set_filtrado(request, tipo='especial')
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']
    for field in campos:
        tabla[field.verbose_name] = []
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")

        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(content_type=content, object_id__in=lista, ** {field.name: 'si'}).count())
    
    totales = get_total(resultados)
    tabla = get_prom_lista_con_total(tabla, totales)

    return render_to_response("monitoreo/generica_1.html", RequestContext(request, locals()))

def hombres_vbg(request):
    """Conoce usted si en su comunidad existen hombres que ejerven VBG"""
    titulo = '¿Conoce usted si en su comunidad existen hombres que ejercen VBG?'
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        
        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=content, object_id__in=lista, conoce_hombres=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def mujeres_vbg(request):
    """Conoce usted si en su comunidad existen mujeres que han vivido VBG"""
    titulo = '¿Conoce usted si en su comunidad existen mujeres que han vivido VBG?'
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=content, object_id__in=lista, conoce_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def vbg_resolver_con(request):
    """Considera usted que la VBG es un asunto que debe ser resuelto con la participacion de"""
    titulo = u'¿Considera que la VBG es un asunto que debe ser resuelto con la participación de?'
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = ResolverVBG.objects.all()
    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(AsuntoPublicoVBG.objects.filter(content_type=content, object_id__in=lista, resolverse_con=op).count())
            
    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():        
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def afeccion_vbg(request):
    """Cree usted que la VBG afecta a las mujeres, la familia y la comunidad?"""
    titulo = u'¿Cree usted que la VBG afecta a las mujeres, la familia y la comunidad?'
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in ['si', 'no']:
            tabla[op.title()].append(EfectoVBG.objects.filter(content_type=content, object_id__in=lista, afecta_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)

    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def como_afecta(request):
    """Como afecta la VBG a las mujeres, comunidad y la familia"""
    titulo = u'¿Como afecta la VBG a las mujeres, comunidad y la familia?'
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = ComoAfecta.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(EfectoVBG.objects.filter(content_type=content, object_id__in=lista, como_afecta=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def conoce_leyes(request):
    """Conoce alguna ley que penaliza la VBG"""
    titulo = u'¿Sabe usted si en Nicaragua existe alguna ley que penaliza la violencia contra las mujeres?'
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in SI_NO_RESPONDE:
        tabla[op[1]] = []
    
    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in SI_NO_RESPONDE:
            tabla[op[1]].append(ConocimientoLey.objects.filter(content_type=content, object_id__in=lista, existe_ley=op[0]).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def prohibido_por_ley(request):
    """Acciones prohibidas por la ley"""
    from models import SI_NO_RESPONDE

    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in ConocimientoLey._meta.fields if field.get_internal_type() == 'IntegerField' and not (field.name == 'existe_ley' or field.name == 'object_id')]
    
    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
                    
            tabla[field.verbose_name][key] = []
            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")

            for op in SI_NO_RESPONDE:                
                tabla[field.verbose_name][key].append(ConocimientoLey.objects.filter(content_type=content, object_id__in=lista, ** {field.name: op[0]}).count())
                
    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)
    return render_to_response("monitoreo/prohibido_por_ley.html", RequestContext(request, locals()))

def hombres_violentos(request):
    titulo = "¿Cree usted que los hombres son violentos debido a?"
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in CausaVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")

            tabla[field.verbose_name].append(CausaVBG.objects.filter(content_type=content, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def hombres_violencia_mujeres(request):
    """Para usted, los hombres ejercen violencia hacia las mujeres porque"""
    titulo = '¿Cree usted que los hombres son violentos debido a?'
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in JustificacionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")

            tabla[field.verbose_name].append(JustificacionVBG.objects.filter(content_type=content, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)

    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def comportamiento(request):
    """Como deben comportarse hombres y mujeres"""
    from models import CREENCIAS_VBG_RESP
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in Creencia._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")

            for op in CREENCIAS_VBG_RESP:
                tabla[field.verbose_name][key].append(Creencia.objects.filter(content_type=content, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)

    return render_to_response("monitoreo/comportamiento.html", RequestContext(request, locals()))

def ayuda_mujer_violencia(request):
    """En el ultimo anio ha ayudado usted a alguna mujer que ha vivido VBG"""
    titulo = u'¿En el último año ha ayudado usted a alguna mujer que ha vivido VBG?'
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")

        for op in ['si', 'no']:
            tabla[op.title()].append(AccionVBG.objects.filter(content_type=content, object_id__in=lista, ha_ayudado=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica_pie.html", RequestContext(request, locals()))

def que_hace_ante_vbg(request):
    """Que hace usted cuando existe una situación de VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in AccionVBG._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    opciones = [1, 2, 3, 4, 5, 6]

    for field in campos:        
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = {}            
                
            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")

            for op in opciones:
                tabla[field.verbose_name][key][op] = AccionVBG.objects.filter(content_type=content, object_id__in=lista, ** {field.name: op-1}).count()
    totales = get_total(resultados)   
            
    return render_to_response("monitoreo/que_hace_ante_vbg.html", RequestContext(request, locals()))

def donde_buscar_ayuda(request):
    titulo = '¿Donde debe buscar ayuda una mujer que vive VBG?'
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = BuscarAyuda.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(AccionVBG.objects.filter(content_type=content, object_id__in=lista, donde_buscar=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def que_debe_hacer(request):    
    titulo = "¿Si un hombre le pega a su pareja que acciones deberia de tomar?"
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = QueDebeHacer.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(AccionVBG.objects.filter(content_type=content, object_id__in=lista, accion_tomar=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)

    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def que_acciones_realizar(request):
    titulo = "¿Cuando una mujer vive VBG cuales acciones deberia realizar?"
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = Decision.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(TomaDecision.objects.filter(content_type=content, object_id__in=lista, decision=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def participacion_en_espacios(request):
    titulo = u"¿En que organización o espacios comunitarios te encuentras integrada/o actualmente?"
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = Espacio.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(ParticipacionPublica.objects.filter(content_type=content, object_id__in=lista, espacio=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

def ha_vivido_vbg(request):
    """Considera usted que alguna vez ha vivido VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")

        for op in ['si', 'no']:
            tabla[op.title()].append(PrevalenciaVBG.objects.filter(content_type=content, object_id__in=lista, ha_vivido_vbg=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/ha_vivido_vbg.html", RequestContext(request, locals()))

def tipo_vbg_vivido(request):
    titulo = u"¿Qué tipo de VBG ha vivido?"
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = TipoVBG.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(PrevalenciaVBG.objects.filter(content_type=content, object_id__in=lista, que_tipo=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/tipo_vbg_vivido.html", RequestContext(request, locals()))

def ha_ejercido_vbg(request):
    """Considera usted que ejercido VBG contra una mujer el ultimo año"""
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")

        for op in ['si', 'no']:
            tabla[op.title()].append(PrevalenciaVBGHombre.objects.filter(content_type=content, object_id__in=lista, ha_vivido_vbg=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/ha_ejercido_vbg.html", RequestContext(request, locals()))

def tipo_vbg_ejercido(request):
    titulo = u"¿Qué tipo de VBG ha ejercido?"
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = TipoVBG.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(PrevalenciaVBGHombre.objects.filter(content_type=content, object_id__in=lista, que_tipo=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/tipo_vbg_ejercido.html", RequestContext(request, locals()))

def actividades_hogar(request):
    """Cuales de las siguientes actividades realiza usted en su hogar"""
    from models import HOGAR
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in Corresponsabilidad._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")

            for op in HOGAR:
                tabla[field.verbose_name][key].append(Corresponsabilidad.objects.filter(content_type=content, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list2(tabla, totales)
    return render_to_response("monitoreo/actividades_hogar.html", RequestContext(request, locals()))

def solucion_problema(request):
    """Que se debe hacer para que la solucion a un conflicto entre la pareja sea exitoso"""
    titulo = u'¿Que se debe hacer para que la solucion a un conflicto entre la pareja sea exitoso?'
    from models import DES_AC    
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in ComunicacionAsertiva._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']
    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            if key < 4:
                content = ContentType.objects.get(app_label="1-principal", model="mujer")
            else:
                content = ContentType.objects.get(app_label="1-principal", model="hombre")
            
            for op in DES_AC:
                tabla[field.verbose_name][key].append(ComunicacionAsertiva.objects.filter(content_type=content, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list3(tabla, totales)

    return render_to_response("monitoreo/solucion_problema.html", RequestContext(request, locals()))

def negociacion_pareja(request):
    """Que se debe hacer para que una negociacion de pareja sea exitosa"""
    titulo = u'¿Que se debe hacer para que una negociacion de pareja sea exitosa?'
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = NegociacionExitosa.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        if key < 4:
            content = ContentType.objects.get(app_label="1-principal", model="mujer")
        else:
            content = ContentType.objects.get(app_label="1-principal", model="hombre")
        for op in opciones:
            tabla[op].append(ComunicacionAsertiva.objects.filter(content_type=content, object_id__in=lista, negociacion_exitosa=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/generica.html", RequestContext(request, locals()))

#obtener la vista adecuada para los indicadores
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
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
    'ha-vivido-vbg': ha_vivido_vbg,
    'tipo-vbg-vivido': tipo_vbg_vivido,
    'ha-ejercido-vbg': ha_ejercido_vbg,
    'tipo-vbg-ejercido': tipo_vbg_ejercido,
    'actividades-hogar': actividades_hogar,
    'solucion-problema': solucion_problema,
    'negociacion-pareja': negociacion_pareja,
    }

#---------------------------- ACA LAS VISTAS PARA FUNCIONARIOS -------------------------------#
cfunc = ContentType.objects.get(app_label="1-principal", model="funcionario")

# funcion para eliminar opciones que suman 0
verificar = lambda x: sum(x)

def le_hablan_de(request):
    titulo = '¿Cuando alguien le habla de VBG usted cree que estan hablando de?'
    encuestas = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = HablanDe.objects.all()
    for op in opciones:
        tabla[op] = []
    
    for op in opciones:
        for key, grupo in encuestas.items():
            tabla[op].append(ConceptoViolencia.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             hablande=op, respuesta='si').count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def expresion_violencia(request):
    titulo = '¿De que manera considera usted que se expresa la violencia?'
    encuestas = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

    for key, grupo in encuestas.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def comportamiento_funcionario(request):
    from models import CREENCIAS_VBG_RESP
    titulo = u'Como deben comportarse hombres y mujeres'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in Creencia._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            for op in CREENCIAS_VBG_RESP:
                tabla[field.verbose_name][key].append(Creencia.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)

    return render_to_response("monitoreo/funcionarios/comportamiento.html", RequestContext(request, locals()))

def hombres_violentos_func(request):
    titulo = '¿Cree usted que los hombres son violentos debido a?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in CausaVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(CausaVBG.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def hombres_violencia_mujeres_func(request):
    titulo = '¿Cree usted que los hombres son violentos debido a?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in JustificacionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(JustificacionVBG.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def prohibido_por_ley_func(request):
    from models import SI_NO_RESPONDE
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in ConocimientoLey._meta.fields if field.get_internal_type() == 'IntegerField' and not (field.name == 'existe_ley' or field.name == 'object_id')]

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = []

            for op in SI_NO_RESPONDE:    
                tabla[field.verbose_name][key].append(ConocimientoLey.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)
    return render_to_response("monitoreo/funcionarios/prohibido_por_ley_func.html", RequestContext(request, locals()))

def ruta_critica(request):
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in RutaCritica._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    opciones = [1, 2, 3, 4, 5]

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = {}

            for op in opciones:
                tabla[field.verbose_name][key][op] = RutaCritica.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: op-1}).count()

    totales = get_total(resultados)
    #tomar todos los valores de la tabla y calcular promedio
#    for key, value in tabla.items():
#        for i in range(1, 3):
#            total = sum(tabla[key][i].values())
#            for nivel in opciones:
#                tabla[key][i][nivel] = [tabla[key][i][nivel], get_prom(tabla[key][i][nivel], total)]

    totales_vertical = []
    grafico = {}
    for a in range(2):        
        counter = 0
        for i in range(5):
            suma = []
            for key, value in tabla.items():
                for k, v in value.items()[a:a + 1]:
                    suma.append(v.values()[counter])
            counter += 1
            totales_vertical.append(sum(suma))   

    for i in range(5):
        grafico[i + 1] = []

    orden = 0
    for a in range(2):        
        counter2 = 0
        for i in range(5):
            for key, value in tabla.items():
                for k, v in value.items()[a:a + 1]:
                    #calcular el promedio de cada valor
                    promedio = get_prom(v.values()[counter2], totales_vertical[orden])
                    #agregar a la tabla el promedio para cada valor
                    tabla[key][a + 1][i + 1] = [v.values()[counter2], promedio]
                    grafico[i + 1].append({key: v.values()[counter2]})
            counter2 += 1
            orden += 1

    return render_to_response("monitoreo/funcionarios/ruta_critica.html", RequestContext(request, locals()))

def registro_datos(request):
    titulo = u'¿Su institución lleva un registro de datos sobre los casos de VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)
    for key in resultados.keys():
        tabla[key] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for opcion in range(1, 3):
            cantidad = RegistroDato.objects.filter(content_type=cfunc, object_id__in=lista, lleva_registro=opcion).count()
            tabla[key][opcion] = [cantidad, get_prom(cantidad, grupo.count())]

    return render_to_response("monitoreo/funcionarios/generica_pie_func.html", 
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def casos_registrados(request):    
    titulo = u'¿Cuántos casos de VBG tienen registrados?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        tabla[key] = RegistroDato.objects.filter(content_type=cfunc, object_id__in=lista).aggregate(casos=Sum('cuantos'))['casos']
    return render_to_response("monitoreo/funcionarios/casos_registrados.html", {'tabla': tabla, 'titulo': titulo, 'totales': totales}, RequestContext(request))

def casos_registrados_por_tipo(request):
    resultados = _query_set_filtrado(request, tipo='funcionario')    
    titulo = u'Qué cantidad de casos de VBG han registrado?'
    campos = [field for field in RegistroDato._meta.fields if field.get_internal_type() == 'IntegerField' and field.name not in ['object_id', 'lleva_registro', 'cuantos']]
    tabla = {}

    for campo in campos:
        tabla[campo.verbose_name] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for campo in campos:
            tabla[campo.verbose_name][key] = RegistroDato.objects.filter(content_type=cfunc, object_id__in=lista).aggregate(cantidad=Sum(campo.name))['cantidad']        

    totales = get_total(resultados)
    return render_to_response("monitoreo/funcionarios/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def calidad_servicios(request):
    from models import SERVICIOS
    titulo = u'¿Cómo valora usted los servicios que su institución ofrece a mujeres que viven VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SERVICIOS:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SERVICIOS:
            tabla[opcion[1]][key] = CalidadAtencionFuncionario.objects.filter(content_type=cfunc, object_id__in=lista, valor_servicio=opcion[0]).count()

    return render_to_response("monitoreo/funcionarios/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def mejorar_atencion(request):
    from models import SI_NO_SIMPLE2
    titulo = u'¿Ha realizado su institución algunas acciones dirigidas a mejorar la atencion a las mujeres?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SI_NO_SIMPLE2:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SI_NO_SIMPLE2:
            tabla[opcion[1]][key] = AccionMejorarAtencion.objects.filter(content_type=cfunc, object_id__in=lista, realizo_accion=opcion[0]).count()

    return render_to_response("monitoreo/funcionarios/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def que_acciones(request):    
    titulo = u'¿Cuáles fueron las acciones que su institución realizó?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = Accion.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(AccionMejorarAtencion.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             cuales=op).count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def prevenir_vbg(request):
    from models import SI_NO_SIMPLE2
    titulo = u'¿Su institución realizo algunas acciones dirigidas a prevenir la VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SI_NO_SIMPLE2:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SI_NO_SIMPLE2:
            tabla[opcion[1]][key] = AccionPrevVBG.objects.filter(content_type=cfunc, object_id__in=lista, realizo_accion=opcion[0]).count()
    return render_to_response("monitoreo/funcionarios/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def cuales_acciones(request):
    titulo = u'¿Cuáles fueron las acciones de prevención de la VBG que su institución realizo?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = AccionPrevencion.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(AccionPrevVBG.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             accion_prevenir=op).count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

#obtener la vista adecuada para los indicadores
def _get_view_funcionario(request, vista):
    if vista in VALID_VIEWS_FUNCIONARIO:
        return VALID_VIEWS_FUNCIONARIO[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS_FUNCIONARIO = {
    #vistas para funcionarios, son un turco pero ni moo :S
    'le-hablan-de': le_hablan_de,
    'expresion-violencia': expresion_violencia,
    'comportamiento': comportamiento_funcionario,
    'hombres-violentos-por': hombres_violentos_func,
    'hombres-violencia-mujeres': hombres_violencia_mujeres_func,
    'prohibido-por-ley': prohibido_por_ley_func,
    'ruta-critica': ruta_critica,
    'registro-datos': registro_datos,
    'casos-registrados': casos_registrados,
    'casos-registrados-por-tipo': casos_registrados_por_tipo,
    'calidad-servicios': calidad_servicios,
    'mejorar-atencion': mejorar_atencion,
    'que-acciones': que_acciones,
    'prevenir-vbg': prevenir_vbg,
    'cuales-acciones': cuales_acciones,
}

#funcion encargada de sacar promedio con los valores enviados
def get_prom(cantidad, total):
    if total == None or cantidad == None or total == 0:
        x = 0
    else:
        x = (cantidad * 100) / float(total)
    return int(round(x, 0))

def get_prom_lista_con_total(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])],
            [value[2], get_prom(value[2], total[2])],
            [value[3], get_prom(value[3], total[3])],
            [value[4], get_prom(value[4], total[4])],
            [value[5], get_prom(value[5], total[5])],
            [value[6], get_prom(value[6], total[6])],
            [value[7], get_prom(value[7], total[7])]]
    return tabla2

def get_prom_lista(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])],
            [value[2], get_prom(value[2], total[2])],
            [value[3], get_prom(value[3], total[3])],
            [value[4], get_prom(value[4], total[4])],
            [value[5], get_prom(value[5], total[5])]]
    return tabla2

def get_prom_lista_func(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])]]
    return tabla2

def get_prom_dead_list(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():                        
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])],
            [value[2], get_prom(value[2], totales[key-1])],
            [value[3], get_prom(value[3], totales[key-1])]]
    return tabla

def get_prom_dead_list2(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])],
            [value[2], get_prom(value[2], totales[key-1])],
            [value[3], get_prom(value[3], totales[key-1])],
            [value[4], get_prom(value[4], totales[key-1])]]
    return tabla

def get_prom_dead_list3(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])]]
    return tabla

def convertir_grafico(tabla):
    """ funcion donde primeros numeros igual: 1 -> m10-13, 2 -> m14-18....
    los siguientes numeros son las opciones "1 -> Si", "2 -> No", "3 -> No sabe", "No responde"
    """
    dicc = {}
    for i in range(1, len(tabla.items()[0][1].keys()) + 1):
        dicc[i] = {}
        for j in range(1, len(tabla.items()[0][1][1]) + 1):
            dicc[i][j] = []

    for i in range(1, len(tabla.items()[0][1].keys()) + 1):
        for j in range(1, len(tabla.items()[0][1][1]) + 1):
            for key, value in tabla.items():
                dicc[i][j].append(value[i][j-1])
    return dicc

#------------------------LIDERES Y LIDEREZAS------------------------------------
def _get_vista_lideres(request, vista):
    if vista in VALID_VIEWS_LIDERES:
        return VALID_VIEWS_LIDERES[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

verificar_dicc = lambda x: x[1] + x[2]

#content type para lider
clider = ContentType.objects.get(app_label="1-principal", model="lider")

def lideres_le_hablan_de(request):
    titulo = '¿Cuando alguien le habla de VBG usted cree que estan hablando de?'
    encuestas = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = HablanDe.objects.all()
    
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in encuestas.items():
            tabla[op].append(ConceptoViolencia.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             hablande=op, respuesta='si').count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def expresion_violencia_lideres(request):
    titulo = '¿De que manera considera usted que se expresa la violencia?'
    encuestas = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']    

    for field in campos:
        tabla[field.verbose_name] = []

    for key, grupo in encuestas.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def comportamiento_lideres(request):
    """Como deben comportarse hombres y mujeres"""
    from models import CREENCIAS_VBG_RESP
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    titulo = 'Como deben comportarse hombres y mujeres'
    campos = [field for field in Creencia._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []           

            for op in CREENCIAS_VBG_RESP:
                tabla[field.verbose_name][key].append(Creencia.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)

    return render_to_response("monitoreo/lideres/comportamiento_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'grafico': grafico, 'totales': totales, 'CREENCIAS_VBG_RESP': CREENCIAS_VBG_RESP},
                              RequestContext(request))

def lideres_hombres_violentos(request):
    titulo = "¿Cree usted que los hombres son violentos debido a?"
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in CausaVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]            

            tabla[field.verbose_name].append(CausaVBG.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def conoce_hombres_violentos(request):
    titulo = u'¿Conoce usted si en su comunidad existen hombres que ejercen VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]       
        
        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=clider, object_id__in=lista, conoce_hombres=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)   

    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def conoce_mujeres_vbg(request):
    titulo = u'¿Conoce usted si en su comunidad existen mujeres que han vivido VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=clider, object_id__in=lista, conoce_mujeres=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def hombres_violencia_mujeres_lideres(request):
    """Para usted, los hombres ejercen violencia hacia las mujeres porque"""
    titulo = u'Para usted, los hombres ejercen violencia hacia las mujeres porque'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in JustificacionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(JustificacionVBG.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def ayuda_mujer_violencia_lideres(request):
    """En el ultimo anio ha ayudado usted a alguna mujer que ha vivido VBG"""
    titulo = u'¿En el último año ha ayudado usted a alguna mujer que ha vivido VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, ha_ayudado=op).count())
            
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def donde_buscar_ayuda_lideres(request):
    titulo = '¿Donde debe buscar ayuda una mujer que vive VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = BuscarAyuda.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]      

        for op in opciones:
            tabla[op].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, donde_buscar=op).count())

    for key, value in tabla.items():
        if verificar(value) < 5:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def ha_vivido_vbg(request):
    titulo = u'¿Considera usted que alguna vez ha vivido VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, ha_vivido_vbg=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def tipo_vbg_ha_vivido(request):
    resultados = _query_set_filtrado(request, tipo='lider')
    titulo = u'¿Qué tipo de VBG ha vivido?'
    tipos = TipoVBG.objects.all()
    tabla = {}

    for tipo in tipos:
        tabla[tipo] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for tipo in tipos:
            tabla[tipo][key] = PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, que_tipo=tipo).count()

    for key, value in tabla.items():        
        if verificar_dicc(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def frecuencia_vbg(request):
    from models import FRECUENCIA
    resultados = _query_set_filtrado(request, tipo='lider')
    titulo = u'¿Con que frecuencia ha vivido situaciones de VBG?'
    tabla = {}

    for tipo in FRECUENCIA:
        tabla[tipo[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for tipo in FRECUENCIA:
            tabla[tipo[1]][key] = PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, frecuencia=tipo[0]).count()

    totales = get_total(resultados)
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def quien_ejercio_vbg(request):
    titulo = u'¿Quién fue la persona que ejecutó esta situación?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    quienes = Quien.objects.all()

    for quien in quienes:
        tabla[quien] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[quien].append(PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, quien=quien).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def conocimiento_leyes(request):
    titulo = u'Acciones son prohibidas por la ley'
    from models import SI_NO_RESPONDE
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in ConocimientoLey._meta.fields if field.get_internal_type() == 'IntegerField' and not (field.name == 'existe_ley' or field.name == 'object_id')]

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = []

            for op in SI_NO_RESPONDE:
                tabla[field.verbose_name][key].append(ConocimientoLey.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)
    return render_to_response("monitoreo/lideres/prohibido_por_ley.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'grafico': grafico, 'SI_NO_RESPONDE': SI_NO_RESPONDE},
                              RequestContext(request))

def decisiones(request):
    titulo = u'¿Cuando una mujer vive VBG cuales acciones deberia realizar?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    quienes = Decision.objects.all()

    for quien in quienes:
        tabla[quien] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[quien].append(TomaDecision.objects.filter(content_type=clider, object_id__in=lista, decision=quien).count())

    for key, value in tabla.items():
        if verificar(value) < 5:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def corresponsabilidad(request):
    titulo = u'¿Cuáles de las siguientes actividades realiza usted en su hogar?'
    from models import HOGAR
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in Corresponsabilidad._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            for op in HOGAR:
                tabla[field.verbose_name][key].append(Corresponsabilidad.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list2(tabla, totales)
    return render_to_response("monitoreo/lideres/corresponsabilidad.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'grafico': grafico, 'HOGAR': HOGAR},
                              RequestContext(request))

def que_debe_hacer_lideres(request):
    titulo = "¿Si un hombre le pega a su pareja que acciones deberia de tomar?"
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = QueDebeHacer.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, accion_tomar=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def prevenir_vbg_lider(request):
    from models import SI_NO_SIMPLE2
    titulo = u'¿En su organización, escuela o usted realizan algunas acciones dirigidas a prevenir la VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SI_NO_SIMPLE2:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SI_NO_SIMPLE2:
            tabla[opcion[1]][key] = AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, ud_previene=opcion[0]).count()
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def cuales_acciones_lideres(request):
    titulo = u'¿Cuáles fueron las acciones de prevención de la VBG que realizo?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = AccionPrevencion.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             accion_prevenir=op).count())
    for key, value in tabla.items():
        if verificar(value) < 5:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def mujeres_lideres(request):
    titulo = u'¿Existen mujeres que representan a otras mujeres?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(IncidenciaPolitica.objects.filter(content_type=clider, object_id__in=lista, existen_mujeres=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))
def nivel_satisfaccion(request):
    from models import SATISFECHAS
    titulo = u'¿Qué tan satisfechas están las mujeres con quienes las representan?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SATISFECHAS:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SATISFECHAS:
            tabla[opcion[1]][key] = IncidenciaPolitica.objects.filter(content_type=clider, object_id__in=lista, satisfecha=opcion[0]).count()
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def presenta_propuestas(request):
    titulo = u'¿Ha presentado propuestas de acciones de prevención de VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=lista, propuesta=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def tipo_propuesta_presentada(request):
    titulo = u'¿Que tipo de propuesta ha presentado?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = TipoPropuesta.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             si_tipo=op).count())
    for key, value in tabla.items():
        if verificar(value) == 1:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def negocia_propuestas(request):
    titulo = u'¿Ha negociado propuestas de acciones de prevención de VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=lista, propuesta2=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def tipo_propuesta_negociada(request):
    titulo = u'¿Que tipo de propuesta ha negociado?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = TipoPropuesta.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             si_tipo2=op).count())
    for key, value in tabla.items():
        if verificar(value) == 1:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def solucion_problema_lideres(request):
    titulo = u'¿Qué se debe hacer para que la solución a un conflicto entre la pareja sea exitoso?'
    from models import DES_AC
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in ComunicacionAsertiva._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']
    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = []
            for op in DES_AC:
                tabla[field.verbose_name][key].append(ComunicacionAsertiva.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list3(tabla, totales)

    return render_to_response("monitoreo/lideres/solucion_problema_lideres.html", RequestContext(request, locals()))

def negociacion_exitosa(request):
    titulo = u'¿Qué se debe hacer para que una negociación de pareja sea exitosa?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = NegociacionExitosa.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(ComunicacionAsertiva.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             negociacion_exitosa=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

VALID_VIEWS_LIDERES = {
    'le-hablan-de': lideres_le_hablan_de, 
    'hombres-violentos': lideres_hombres_violentos, 
    'comportamiento': comportamiento_lideres,
    'justificacion': hombres_violencia_mujeres_lideres,
    'ayuda-mujer': ayuda_mujer_violencia_lideres,
    'donde-buscar-ayuda': donde_buscar_ayuda_lideres,
    'expresion-violencia': expresion_violencia_lideres,
    'conoce-hombres-violentos': conoce_hombres_violentos,
    'conoce-mujeres-vbg': conoce_mujeres_vbg,
    'ha-vivido-vbg': ha_vivido_vbg,
    'tipo-vbg-ha-vivido': tipo_vbg_ha_vivido,
    'frecuencia-vbg': frecuencia_vbg,
    'quien-ejercio-vbg': quien_ejercio_vbg,
    'conocimiento-leyes': conocimiento_leyes,
    'decisiones': decisiones,
    'corresponsabilidad': corresponsabilidad,
    #aca la tabla fea
    'que-debe-hacer': que_debe_hacer_lideres,
    'prevenir-vbg': prevenir_vbg_lider,
    'cuales-acciones': cuales_acciones_lideres,
    'mujeres-lideres': mujeres_lideres,
    'nivel-satisfaccion': nivel_satisfaccion,
    'presenta-propuestas': presenta_propuestas,
    'negocia-propuestas': negocia_propuestas,
    'tipo-propuesta-presentada': tipo_propuesta_presentada,
    'tipo-propuesta-negociada': tipo_propuesta_negociada,
    'solucion-problema-lideres': solucion_problema_lideres,
    'negociacion-exitosa': negociacion_exitosa,
}
