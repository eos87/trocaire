from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import get_model
from trocaire.encuesta.views import consultar
from trocaire.mujeres_hombres.views import *
from trocaire.utils import get_content_type, _query_set_filtrado
from trocaire.encuesta.models import *
from forms import MujerCrucesForm

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
                request.session['mujer_var2'] = request.POST['variable_2']
                return HttpResponseRedirect('mujeres/')
        elif '_crucehombre' in request.POST:
            pass
    else:           
        form = MujerCrucesForm()
    return render_to_response('pf/cruces.html', RequestContext(request, locals()))


OPCIONES_VAR1_MUJER = {1: NIVEL_EDUCATIVO}
MODELO_VAR1_MUJER = {1: 'InformacionSocioEconomica'}
CAMPO_VAR1_MUJER = {1: 'nivel_educativo'}

def cruce_mujeres(request):
    var1 = int(request.session['mujer_var1'])
    resultados = _query_set_filtrado(request, 'solomujeres')
    tabla = {}      
    modelo = get_model('encuesta', MODELO_VAR1_MUJER[var1])
    dicc = _query_set_cruce(request, var1)
    
#    for op in OPCIONES_VAR1_MUJER[var1]:
#        tabla[op].append(ConceptoViolencia.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in resultados], \
#                             hablande=op, respuesta='si').count())
        
    return render_to_response('pf/cruce_mujeres.html', RequestContext(request, locals()))        
       

def _query_set_cruce(request, var1):
    dicc = {}
    model = get_model('encuesta', MODELO_VAR1_MUJER[var1])
    
    for op in OPCIONES_VAR1_MUJER[var1]:
        objs = model.objects.filter(content_type=get_content_type('mujeres'), ** {CAMPO_VAR1_MUJER[var1]: op[0]})
        dicc[op[0]] = [obj.object_id for obj in objs]
        
    return dicc
    
