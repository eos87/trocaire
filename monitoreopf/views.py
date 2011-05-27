from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import get_model
from trocaire.encuesta.views import consultar
from trocaire.mujeres_hombres.views import *
from trocaire.utils import get_content_type, _query_set_filtrado
from trocaire.encuesta.models import *
from forms import MujerCrucesForm, VARIABLE_MUJER_1, VARIABLE_MUJER_2


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
            form = MujerCrucesForm(request.POST)
            if form.is_valid():
                request.session['mujer_var1'] = request.POST['variable_1']
                request.session['mujer_var1_nombre'] = VARIABLE_MUJER_1[int(request.POST['variable_1'])-1][1]
                request.session['mujer_var2'] = request.POST['variable_2']
                request.session['mujer_var2_nombre'] = VARIABLE_MUJER_2[int(request.POST['variable_2'])-1][1]
                request.session['mujer_var2'] = request.POST['variable_2']

                return HttpResponseRedirect('mujeres/')
        elif '_crucehombre' in request.POST:
            pass
    else:           
        form = MujerCrucesForm()
    return render_to_response('pf/cruces.html', RequestContext(request, locals()))


OPCIONES_VAR1_MUJER = {1: NIVEL_EDUCATIVO, 2: SI_NO_SIMPLE, 4: SI_NO_SIMPLE, 5: ESTADO_CIVIL}
MODELO_VAR1_MUJER = {1: 'InformacionSocioEconomica', 2: 'InformacionSocioEconomica', 4: 'InformacionSocioEconomica', 5: 'Mujer'}
CAMPO_VAR1_MUJER = {1: 'nivel_educativo', 2: 'trabaja_fuera', 4: 'estudia', 5: 'estado_civil'}
TIPO_RELACION_VAR1_MUJER = {1: 'generica', 2: 'generica', 4: 'generica', 5: 'normal'}

OPCIONES_VAR2_MUJER = {1: SI_NO_SIMPLE, 2: TipoVBG.objects.all(), 3: FRECUENCIA, 4: Quien.objects.all(), 5: SERVICIOS}
MODELO_VAR2_MUJER = {1: 'PrevalenciaVBG', 2: 'PrevalenciaVBG', 3: 'PrevalenciaVBG', 4: 'PrevalenciaVBG', 5: 'CalidadAtencion'}
CAMPO_VAR2_MUJER = {1: 'ha_vivido_vbg', 2: 'que_tipo', 3: 'frecuencia', 4: 'quien', 5: 'valor_servicio'}
TIPO_OPCION_VAR2_MUJER = {1: 'tupla', 2: 'queryset', 3: 'tupla', 4: 'queryset', 5: 'tupla'}

def cruce_mujeres(request):
    var1 = int(request.session['mujer_var1'])
    var2 = int(request.session['mujer_var2'])    
    dicc = _query_set_cruce(request, var1)
    tabla = {}      
    modelo_var2 = get_model('encuesta', MODELO_VAR2_MUJER[var2])
    total_var1 = {}
    total_var2 = {}
    
    for op in OPCIONES_VAR2_MUJER[var2]:
        #obtener el tipo de opcion
        if TIPO_OPCION_VAR2_MUJER[var2] == 'tupla':
            llave = op[1]
            opcion = op[0]
        elif TIPO_OPCION_VAR2_MUJER[var2] == 'queryset':
            llave = op
            opcion = op
            
        tabla[llave] = {}
        for key, ids in dicc.items():
            tabla[llave][key] = modelo_var2.objects.filter(content_type=get_content_type('mujeres'), 
                                                           object_id__in=ids, 
                                                           ** {CAMPO_VAR2_MUJER[var2]: opcion}).count()
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
    resultados = _query_set_filtrado(request, 'solomujeres')
    dicc = {}
    #decidir el app_label segun el modelo
    if TIPO_RELACION_VAR1_MUJER[var1] == 'generica':
        _app_label = 'encuesta'
    elif TIPO_RELACION_VAR1_MUJER[var1] == 'normal':
        _app_label = '1-principal' 
    
    #obtener el modelo a consultar
    model = get_model(_app_label, MODELO_VAR1_MUJER[var1])
        
    for op in OPCIONES_VAR1_MUJER[var1]:
        #validar si el modelo es generico o normal
        if TIPO_RELACION_VAR1_MUJER[var1] == 'generica':
            objs = model.objects.filter(content_type=get_content_type('mujeres'), 
                                        object_id__in=[encuesta.id for encuesta in resultados],
                                        ** {CAMPO_VAR1_MUJER[var1]: op[0]})            
            dicc[op[1]] = [obj.object_id for obj in objs]
            
        elif TIPO_RELACION_VAR1_MUJER[var1] == 'normal':
            objs = model.objects.filter(id__in=[encuesta.id for encuesta in resultados],
                                        ** {CAMPO_VAR1_MUJER[var1]: op[0]})
            dicc[op[1]] = [obj.id for obj in objs]
        
    return dicc
