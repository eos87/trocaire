from django.shortcuts import render_to_response
from django.template.context import RequestContext
from trocaire.encuesta.views import consultar

def consultarpf(request):
    request.session['centinela'] = 0  
    return consultar(request, pf=True)