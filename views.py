from django.http import HttpResponse
from trocaire.lugar.models import *
from trocaire.encuesta.models import *
import simplejson

def get_depas(request):
    id = request.GET.get('id', '')
    depas = Departamento.objects.filter(pais__pk=int(id)).values('id', 'nombre')

    return HttpResponse(simplejson.dumps(list(depas)), mimetype='application/json')

def get_munis(request):
    id = request.GET.get('id', '')
    depas = Municipio.objects.filter(departamento__pk=int(id)).values('id', 'nombre')

    return HttpResponse(simplejson.dumps(list(depas)), mimetype='application/json')

def __get_data(request):
    id = request.GET.get('id', '')
    org = Contraparte.objects.get(pk=int(id))
    values = []
    values.append(org.departamento.id)
    values.append(org.municipio.id)

    return HttpResponse(simplejson.dumps(values), mimetype='application/json')