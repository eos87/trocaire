from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import get_model
from trocaire.encuesta.views import consultar
from trocaire.mujeres_hombres.views import *
from trocaire.utils import get_content_type, _query_set_filtrado
from trocaire.encuesta.models import *
from forms import MujerCrucesForm, VARIABLE_MUJER_1, VARIABLE_MUJER_2
from forms import HombreCrucesForm, VARIABLE_HOMBRE_1, VARIABLE_HOMBRE_2


def consultarpf(request):
    request.session['centinela'] = 0
    return consultar(request, pf=1)

def proposito(request):
    return render_to_response('pf/proposito.html', RequestContext(request, locals()))

def fin(request):
    return render_to_response('pf/fin.html', RequestContext(request, locals()))

#vista disenada para realizar los cruces de variables
def filtro_cruces(request):
    if request.method == 'POST':
        if '_crucemujer' in request.POST:
            form2 = HombreCrucesForm()
            form = MujerCrucesForm(request.POST)
            if form.is_valid():
                request.session['var1'] = request.POST['variable_1']
                request.session['var1_nombre'] = VARIABLE_MUJER_1[int(request.POST['variable_1'])-1][1]
                request.session['var2'] = request.POST['variable_2']
                request.session['var2_nombre'] = VARIABLE_MUJER_2[int(request.POST['variable_2'])-1][1]
                request.session['var2'] = request.POST['variable_2']
                request.session['content_type'] = 'mujeres'
                
                return HttpResponseRedirect('mujeres/')
            
        elif '_crucehombre' in request.POST:
            form = MujerCrucesForm()
            form2 = HombreCrucesForm(request.POST)
            if form2.is_valid():
                request.session['var1'] = request.POST['variable_hombre_1']
                request.session['var1_nombre'] = VARIABLE_HOMBRE_1[int(request.POST['variable_hombre_1'])-6][1]
                request.session['var2'] = request.POST['variable_hombre_2']
                request.session['var2_nombre'] = VARIABLE_HOMBRE_2[int(request.POST['variable_hombre_2'])-7][1]
                request.session['var2'] = request.POST['variable_hombre_2']
                request.session['content_type'] = 'hombres'
                
                return HttpResponseRedirect('hombres/')
    else:
        form = MujerCrucesForm()
        form2 = HombreCrucesForm()
    return render_to_response('pf/cruces.html', RequestContext(request, locals()))

#----------------- programacion para cruces de variables de mujeres ---------------------------------
#DATOS DE VARIABLE NUMERO 1
OPCIONES_VAR1 = {1: NIVEL_EDUCATIVO, 2: SI_NO_SIMPLE, 3: ((0,0), (1,2), (3,4), (5,5)), 4: SI_NO_SIMPLE,
                 5: ESTADO_CIVIL, 6: NIVEL_EDUCATIVO, 7: SI_NO_SIMPLE, 8: ESTADO_CIVIL}

MODELO_VAR1 = {1: 'InformacionSocioEconomica', 2: 'InformacionSocioEconomica', 3: 'ComposicionHogar', 4: 'InformacionSocioEconomica',
               5: 'Mujer', 6: 'InformacionSocioEconomica', 7: 'InformacionSocioEconomica', 8: 'Hombre'}

CAMPO_VAR1 = {1: 'nivel_educativo', 2: 'trabaja_fuera', 3: 'cuantos_hijos', 4: 'estudia',
              5: 'estado_civil', 6: 'nivel_educativo', 7: 'trabaja_fuera', 8: 'estado_civil'}

TIPO_RELACION_VAR1 = {1: 'generica', 2: 'generica', 3: 'rango', 4: 'generica',
                      5: 'normal', 6: 'generica', 7: 'generica', 8: 'normal'}

#DATOS DE VARIABLE NUMERO 2
OPCIONES_VAR2 = {1: SI_NO_SIMPLE, 2: TipoVBG.objects.all(),
                 3: FRECUENCIA, 4: Quien.objects.all(),
                 5: SERVICIOS, 6: ComoAfecta.objects.all(),
                 7: SI_NO_SIMPLE, 8: TipoVBG.objects.all(),
                 9: FRECUENCIA2, 10: Quien2.objects.all(), 11: ComoAfecta.objects.all()}

#modelo padre de la variable a cruzar
MODELO_VAR2 = {1: 'PrevalenciaVBG', 2: 'PrevalenciaVBG',
               3: 'PrevalenciaVBG', 4: 'PrevalenciaVBG',
               5: 'CalidadAtencion', 6: 'EfectoVBG',
               7: 'PrevalenciaVBGHombre', 8: 'PrevalenciaVBGHombre',
               9: 'PrevalenciaVBGHombre', 10: 'PrevalenciaVBGHombre',
               11: 'EfectoVBG'}

#campo necesario para hacer la consulta
CAMPO_VAR2 = {1: 'ha_vivido_vbg', 2: 'que_tipo', 3: 'frecuencia',
              4: 'quien', 5: 'valor_servicio', 6: 'como_afecta',
              7: 'ha_vivido_vbg', 8: 'que_tipo', 9: 'frecuencia',
              10: 'quien', 11: 'como_afecta'}

#tipo de opciones ya se tupla o queryset
TIPO_OPCION_VAR2 = {1: 'tupla', 2: 'queryset', 3: 'tupla',
                    4: 'queryset', 5: 'tupla', 6: 'queryset',
                    7: 'tupla', 8: 'queryset', 9: 'tupla',
                    10: 'queryset', 11: 'queryset'}

def cruce_mujeres(request):
    var1 = int(request.session['var1'])
    var2 = int(request.session['var2'])
    dicc = _query_set_cruce(request, var1)
    tabla = {}
    modelo_var2 = get_model('encuesta', MODELO_VAR2[var2])
    total_var1 = {}
    total_var2 = {}
    
    for op in OPCIONES_VAR2[var2]:
        #obtener el tipo de opcion
        if TIPO_OPCION_VAR2[var2] == 'tupla':
            llave = op[1]
            opcion = op[0]
        elif TIPO_OPCION_VAR2[var2] == 'queryset':
            llave = op
            opcion = op
            
        tabla[llave] = {}
        for key, ids in dicc.items():
            tabla[llave][key] = modelo_var2.objects.filter(content_type=get_content_type(request.session['content_type']),
                                                           object_id__in=ids,
                                                           ** {CAMPO_VAR2[var2]: opcion}).count()
        #calcular los totales para variable2
        total_var2[llave] = sum(tabla[llave].values())
    
    #calcular los totales variable1
    for key in dicc.keys():
        total_var1[key] = 0
        for k,v in tabla.items():
            total_var1[key] += tabla[k][key]
    
    #calcular el total general
    total_general = sum(total_var1.values())    
    
    return render_to_response('pf/cruce_mujeres.html', RequestContext(request, locals()))
       

def _query_set_cruce(request, var1):
    if request.session['content_type'] == 'mujeres':
        resultados = _query_set_filtrado(request, 'solomujeres')
    else:
        resultados = _query_set_filtrado(request, 'solohombres')
    dicc = {}
    #decidir el app_label segun el modelo
    if TIPO_RELACION_VAR1[var1] == 'generica':
        _app_label = 'encuesta'
    elif TIPO_RELACION_VAR1[var1] == 'normal':
        _app_label = '1-principal'
    elif TIPO_RELACION_VAR1[var1] == 'rango':
        _app_label = 'encuesta'
    
    #obtener el modelo a consultar
    model = get_model(_app_label, MODELO_VAR1[var1])
        
    for op in OPCIONES_VAR1[var1]:
        #validar si el modelo es generico o normal
        if TIPO_RELACION_VAR1[var1] == 'generica':
            objs = model.objects.filter(content_type=get_content_type(request.session['content_type']),
                                        object_id__in=[encuesta.id for encuesta in resultados],
                                        ** {CAMPO_VAR1[var1]: op[0]})
            dicc[op[1]] = [obj.object_id for obj in objs]
            
        elif TIPO_RELACION_VAR1[var1] == 'normal':
            objs = model.objects.filter(id__in=[encuesta.id for encuesta in resultados],
                                        ** {CAMPO_VAR1[var1]: op[0]})
            dicc[op[1]] = [obj.id for obj in objs]
        
        elif TIPO_RELACION_VAR1[var1] == 'rango':
            params = {}
            if op == (0,0):
                key = 'No tiene'
                params['tiene_hijos'] = 'no'
            elif op == (5,5):
                key = '5+ hijos'
                params['%s__gte' % CAMPO_VAR1[var1]] = op[0]
            elif op != (5,5):
                key = '%s-%s hijos' % (op[0], op[1])
                params['%s__range' % CAMPO_VAR1[var1]] = op
                
            objs = model.objects.filter(content_type=get_content_type(request.session['content_type']),
                                        object_id__in=[encuesta.id for encuesta in resultados],
                                         ** params)
            dicc[key] = [obj.object_id for obj in objs]
                                                                                                                                      
    return dicc


