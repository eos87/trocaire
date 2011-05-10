# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import ViewDoesNotExist
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
        dicc[2] = Mujer.objects.filter(edad__range=(14, 18), ** params)
        dicc[3] = Mujer.objects.filter(edad__gt=18, ** params)

        dicc[4] = Hombre.objects.filter(edad__range=(10, 13), ** params)
        dicc[5] = Hombre.objects.filter(edad__range=(14, 18), ** params)
        dicc[6] = Hombre.objects.filter(edad__gt=18, ** params)
        return dicc

def hablan_de(request):
    """Vista sobre: Cuando alguien le habla de VBG usted cree que estan hablando de:"""    
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = HablanDe.objects.all()
    
    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for concepto in encuesta.concepto_violencia.all():
                lista.append(concepto.pk)
        for opcion in opciones:
            query = ConceptoViolencia.objects.filter(pk__in=lista, hablande=opcion, respuesta='si')
            tabla[opcion].append(query.count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():        
        if checkvalue(value) == 0:
            del tabla[key]
            
    totales = get_total(resultados)    
    tabla = get_prom_lista(tabla, totales)

    return render_to_response("monitoreo/hablan_de.html", RequestContext(request, locals()))

def expresion_vbg(request):
    """Vista sobre: De que manera cree usted que se expresa la VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']
    for field in campos:
        tabla[field.verbose_name] = []
    
    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for expresion in encuesta.expresion_violencia.all():
                lista.append(expresion.pk)    
        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(pk__in=lista, ** {field.name: 'si'}).count())       
    
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)

    return render_to_response("monitoreo/expresion_vbg.html", RequestContext(request, locals()))

def hombres_vbg(request):
    """Conoce usted si en su comunidad existen hombres que ejerven VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for situacion in encuesta.situacion.all():
                lista.append(situacion.pk)
        for op in ['si', 'no']:
            tabla[op].append(SituacionVBG.objects.filter(pk__in=lista, conoce_hombres=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/hombres_vbg.html", RequestContext(request, locals()))

def mujeres_vbg(request):
    """Conoce usted si en su comunidad existen mujeres que han vivido VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for situacion in encuesta.situacion.all():
                lista.append(situacion.pk)
        for op in ['si', 'no']:
            tabla[op].append(SituacionVBG.objects.filter(pk__in=lista, conoce_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/mujeres_vbg.html", RequestContext(request, locals()))

def vbg_resolver_con(request):
    """Considera usted que la VBG es un asunto que debe ser resuelto con la participacion de"""
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = ResolverVBG.objects.all()
    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for resolutor in encuesta.asunto_publico.all():
                lista.append(resolutor.pk)
        for op in opciones:
            tabla[op].append(AsuntoPublicoVBG.objects.filter(pk__in=lista, resolverse_con=op).count())
            
    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():        
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    return render_to_response("monitoreo/vbg_resolver_con.html", RequestContext(request, locals()))

def afeccion_vbg(request):
    """Cree usted que la VBG afecta a las mujeres, la familia y la comunidad?"""
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in ['si', 'no']:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for efecto in encuesta.efecto.all():
                lista.append(efecto.pk)
        for op in ['si', 'no']:
            tabla[op].append(EfectoVBG.objects.filter(pk__in=lista, afecta_mujeres=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)

    return render_to_response("monitoreo/afeccion_vbg.html", RequestContext(request, locals()))

def como_afecta(request):
    """Como afecta la VBG a las mujeres, comunidad y la familia"""
    resultados = _query_set_filtrado(request)
    tabla = {}
    opciones = ComoAfecta.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for efecto in encuesta.efecto.all():
                lista.append(efecto.pk)
        for op in opciones:
            tabla[op].append(EfectoVBG.objects.filter(pk__in=lista, como_afecta=op).count())

    checkvalue = lambda x: sum(x)
    for key, value in tabla.items():
        if checkvalue(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    
    return render_to_response("monitoreo/como_afecta.html", RequestContext(request, locals()))

def conoce_leyes(request):
    """Conoce alguna ley que penaliza la VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}

    for op in SI_NO_RESPONDE:
        tabla[op[1]] = []
    
    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for conocimiento in encuesta.conocimiento.all():
                lista.append(conocimiento.pk)

        for op in SI_NO_RESPONDE:
            tabla[op[1]].append(ConocimientoLey.objects.filter(pk__in=lista, existe_ley=op[0]).count())
    totales = get_total(resultados)
    tabla = get_prom_lista(tabla, totales)
    
    return render_to_response("monitoreo/conoce_leyes.html", RequestContext(request, locals()))

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
    """Cree usted que los hombres son violentos debido a"""
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
    
    return render_to_response("monitoreo/hombres_violentos.html", RequestContext(request, locals()))

def hombres_violencia_mujeres(request):
    """Para usted, los hombres ejercen violencia hacia las mujeres porque"""
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

    return render_to_response("monitoreo/hombres_violencia_mujeres.html", RequestContext(request, locals()))

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
    return render_to_response("monitoreo/ayuda_mujer_violencia.html", RequestContext(request, locals()))

def que_hace_ante_vbg(request):
    """Que hace usted cuando existe una situación de VBG"""
    resultados = _query_set_filtrado(request)
    tabla = {}
    campos = [field for field in AccionVBG._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    opciones = [1,2,3,4,5,6]

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
    }

#funcion encargada de sacar promedio con los valores enviados
def get_prom(cantidad, total):
    if total == None or cantidad == None or total == 0:
        x = 0
    else:
        x = (cantidad * 100) / float(total)
    return round(x, 2)

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

def get_prom_dead_list(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():                        
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])],
            [value[2], get_prom(value[2], totales[key-1])],
            [value[3], get_prom(value[3], totales[key-1])]]
    return tabla

def convertir_grafico(tabla):
    """ funcion donde primeros numeros igual: 1 -> m10-13, 2 -> m14-18....
    los siguientes numeros son las opciones "1 -> Si", "2 -> No", "3 -> No sabe", "No responde"
    """
    dicc = {}
    for i in range(1, 7):
        dicc[i] = {}
        for j in range(1, 5):
            dicc[i][j] = []

    for i in range(1, 7):
        for j in range(1, 5):
            for key, value in tabla.items():
                dicc[i][j].append(value[i][j-1])

    return dicc

