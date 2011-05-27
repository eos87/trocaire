# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from trocaire.encuesta.models import Funcionario
from trocaire.encuesta.models import Hombre
from trocaire.encuesta.models import Lider
from trocaire.encuesta.models import Mujer
from trocaire.lugar.models import Departamento
from trocaire.lugar.models import Municipio


#funcion destinada a devolver las encuestas en rangos de edad
def _query_set_filtrado(request, tipo='mujer'):
    params = {}
    #validar y crear los filtros de la consulta
    if request.session['year']:
        params['fecha__year'] = request.session['year']
       
    if request.session['pais']:
        if request.session['departamento']:
            if request.session['organizacion']:
                params['contraparte__in'] = request.session['organizacion']
            if request.session['municipio']:
                params['municipio__in'] = request.session['municipio']
            if not request.session['organizacion'] and not request.session['municipio']:
                params['municipio__in'] = Municipio.objects.filter(departamento__in=request.session['departamento'])
        else:
            params['municipio__in'] = Municipio.objects.filter(departamento__in=Departamento.objects.filter(pais__in=request.session['pais']))
            
    dicc = {}
    if tipo == 'mujer':
        dicc[1] = Mujer.objects.filter(edad__range=(10, 13), ** params)
        dicc[2] = Mujer.objects.filter(edad__range=(14, 17), ** params)
        dicc[3] = Mujer.objects.filter(edad__gt=18, ** params)
        dicc[4] = Hombre.objects.filter(edad__range=(10, 13), ** params)
        dicc[5] = Hombre.objects.filter(edad__range=(14, 17), ** params)
        dicc[6] = Hombre.objects.filter(edad__gt=18, ** params)
        return dicc

    if tipo == 'mujeres':
        dicc[1] = Mujer.objects.filter(edad__range=(10, 13), ** params)
        dicc[2] = Mujer.objects.filter(edad__range=(14, 17), ** params)
        dicc[3] = Mujer.objects.filter(edad__gte=18, ** params)
        dicc[4] = Mujer.objects.filter(** params)
        return dicc

    if tipo == 'hombres':        
        dicc[1] = Hombre.objects.filter(edad__range=(10, 13), ** params)
        dicc[2] = Hombre.objects.filter(edad__range=(14, 17), ** params)
        dicc[3] = Hombre.objects.filter(edad__gte=18, ** params)
        dicc[4] = Hombre.objects.filter(** params)
        return dicc
    
    elif tipo == 'funcionario':
        dicc[1] = Funcionario.objects.filter(sexo='femenino', ** params)
        dicc[2] = Funcionario.objects.filter(sexo='masculino', ** params)
        return dicc
    
    elif tipo == 'lider':
        dicc[1] = Lider.objects.filter(sexo='femenino', ** params)
        dicc[2] = Lider.objects.filter(sexo='masculino', ** params)
        return dicc
    
    #consultas realizadas para cruces de variables
    elif tipo == 'solomujeres':
        return Mujer.objects.filter(** params)

#funcion lambda que calcula los totales a partir de la consulta filtrada
get_total = lambda x: [v.count() for k, v in x.items()]

#funcion para obtener el content_type adecuado
def get_content_type(tipo='mujeres'):
    if tipo == 'mujeres':
        return ContentType.objects.get(app_label="1-principal", model="mujer")
    elif tipo == 'hombres':
        return ContentType.objects.get(app_label="1-principal", model="hombre")

#funcion para retornar una la tabla con promedios y total
def get_list_with_total(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])],
            [value[2], get_prom(value[2], total[2])],
            [value[3], get_prom(value[3], total[3])]]
    return tabla2

#funcion encargada de sacar promedio con los valores enviados
def get_prom(cantidad, total):
    if total == None or cantidad == None or total == 0:
        x = 0
    else:
        x = (cantidad * 100) / float(total)
    return int(round(x, 0))

#funcion para calcular no se que
def get_prom_dead_list(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])],
            [value[2], get_prom(value[2], totales[key-1])],
            [value[3], get_prom(value[3], totales[key-1])]]
    return tabla

def get_prom_dead_list2(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])],
            [value[2], get_prom(value[2], totales[key-1])],
            [value[3], get_prom(value[3], totales[key-1])],
            [value[4], get_prom(value[4], totales[key-1])]]
    return tabla

def get_prom_dead_list3(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key-1])],
            [value[1], get_prom(value[1], totales[key-1])]]
    return tabla

def convertir_grafico(tabla):
    """ funcion donde primeros numeros igual: 1 -> m10-13, 2 -> m14-18....
    los siguientes numeros son las opciones "1 -> Si", "2 -> No", "3 -> No sabe", "No responde"
    """
    dicc = {}
    for i in range(1, len(tabla.items()[0][1].keys()) + 1):
        dicc[i] = {}
        for j in range(1, len(tabla.items()[0][1][1]) + 1):
            dicc[i][j] = []

    for i in range(1, len(tabla.items()[0][1].keys()) + 1):
        for j in range(1, len(tabla.items()[0][1][1]) + 1):
            for key, value in tabla.items():
                dicc[i][j].append(value[i][j-1])
    return dicc