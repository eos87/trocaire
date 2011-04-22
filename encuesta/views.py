# -*- coding: UTF-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import ConsultarForm

def consultar(request):
	if request.method == 'POST':
		pass
	else:
		form = ConsultarForm()
	return render_to_response("monitoreo/consultar.html", RequestContext(request, locals()))