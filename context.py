def variables(request):
    try:
        centinela = request.session['centinela']
    except:
        centinela = 0
    dicc = {
        'centinela': centinela,
    }
    return dicc