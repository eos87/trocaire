def variables(request):
    dicc = {
        'centinela': request.session['centinela'],
    }
    return dicc