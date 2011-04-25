# -*- coding: UTF-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from forms import ConsultarForm
from trocaire.lugar.models import *
from models import *

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
	encuestas = _query_set_filtrado(request)
	return render_to_response("monitoreo/hablan_de.html", RequestContext(request, locals()))
	

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
		else:
			params['municipio__in'] = Municipio.objects.filter(departamento__in=Departamento.objects.filter(pais__in=request.session['pais']))		
			
	if tipo == 'mujer':
		return Mujer.objects.filter(**params)
	else:
		pass
	
#obtener la vista adecuada para los indicadores
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'hablan-de': hablan_de,    
    }
