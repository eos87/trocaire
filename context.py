def variables(request):
    try:
        centinela = request.session['centinela']
    except:
        centinela = 0
    dicc = {
        'centinela': centinela,
	'request': request,
    }
    return dicc
