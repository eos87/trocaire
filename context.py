def variables(request):
    try:
        centinela = request.session['centinela']
    except:
        pass
    dicc = {
        'centinela': centinela,
    }
    return dicc