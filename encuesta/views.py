# -*- coding: UTF-8 -*-
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

def hablan_de(request):
    """Vista sobre: Cuando alguien le habla de VBG usted cree que estan hablando de:"""    
    resultados = _query_set_filtrado(request)
    print resultados.keys()
    
    tabla = {}    
    for op in HablanDe.objects.all():
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        for encuesta in grupo:
            for concepto in encuesta.concepto_violencia.all():
                lista.append(concepto.pk)
        for opcion in HablanDe.objects.all():
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
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type()=='CharField']
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

#funcion destinada a devolver las encuestas en rangos de edad
def _query_set_filtrado(request, tipo='mujer'):
    params = {}
    #validar y crear los filtros de la consulta
    if request.session['year']:
        params['fecha__year'] = request.session['year']
		
    if request.session['nivel_educativo']:
        params['informacionsocio__in'] = InformacionSocioEconomica.objects.filter(nivel_educativo=request.session['nivel_educativo'])
		
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
	
#obtener la vista adecuada para los indicadores
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'hablan-de': hablan_de,
    'expresion-vbg': expresion_vbg,
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