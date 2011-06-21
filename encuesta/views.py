# -*- coding: UTF-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import ViewDoesNotExist
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import ConsultarForm
from models import *
from trocaire.lugar.models import *
from trocaire.utils import _query_set_filtrado, get_total, get_prom

def generales(request):
    '''Vista para generar tablas de datos generales'''
    total_mujeres = Mujer.objects.all().count() + Lider.objects.filter(sexo='femenino').count() + Funcionario.objects.filter(sexo='femenino').count() 
    total_hombres = Hombre.objects.all().count() + Lider.objects.filter(sexo='masculino').count() + Funcionario.objects.filter(sexo='masculino').count()    
    total =  total_mujeres + total_hombres
    
    tabla_hombre_mujer = {1: {'nombre': 'Mujeres', 'frecuencia': total_mujeres, 'porcentaje': get_prom(total_mujeres, total)},
                          2: {'nombre': 'Hombres', 'frecuencia': total_hombres, 'porcentaje': get_prom(total_hombres, total)}}
    
    tabla_municipio = {}
    dicc = {}        
    for municipio in Municipio.objects.all().order_by('nombre'):
        frecuencia = Mujer.objects.filter(municipio=municipio).count() + Hombre.objects.filter(municipio=municipio).count() + \
                     Lider.objects.filter(municipio=municipio).count() + Funcionario.objects.filter(municipio=municipio).count()
        
        if frecuencia != 0:            
            dicc[municipio] = frecuencia
    
    #ordenar el dicc    
    dicc2 = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    counter_municipio = 1       
    #generar la tabla con los datos a partir del dicc ordenado
    for value in dicc2:
        tabla_municipio[counter_municipio] = {'nombre': '%s - %s' % (value[0].departamento.nombre, value[0].nombre), 'frecuencia': value[1], 'porcentaje': get_prom(value[1], total)}
        counter_municipio += 1
    
    #datos para estado civil
    counter_civil = 1
    tabla_civil = {}
    for op in ESTADO_CIVIL:
        frecuencia = Mujer.objects.filter(estado_civil=op[0]).count() + Hombre.objects.filter(estado_civil=op[0]).count() + \
                     Lider.objects.filter(estado_civil=op[0]).count() + Funcionario.objects.filter(estado_civil=op[0]).count()
        counter_civil += 1
        tabla_civil[counter_civil] = {'nombre': op[1], 'frecuencia': frecuencia, 'porcentaje': get_prom(frecuencia, total)}
        
    #datos para asistencia a iglesia
    counter_iglesia = 1
    tabla_iglesia = {}
    iglesia = {True: 'Si asiste', False: 'No asiste'}
    for op in [True, False]:
        frecuencia = Mujer.objects.filter(asiste_iglesia=op).count() + Hombre.objects.filter(asiste_iglesia=op).count() + \
                     Lider.objects.filter(asiste_iglesia=op).count() + Funcionario.objects.filter(asiste_iglesia=op).count()
        counter_iglesia += 1
        tabla_iglesia[counter_iglesia] = {'nombre': iglesia[op], 'frecuencia': frecuencia, 'porcentaje': get_prom(frecuencia, total)}        
                     
    return render_to_response("generales.html", RequestContext(request, locals()))

def consultar(request, pf=False):    
    if pf:
        request.session['pf'] = True
    else:
        request.session['pf'] = False
            
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            request.session['year'] = form.cleaned_data['year']            
            request.session['pais'] = form.cleaned_data['pais']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['centinela'] = 1
            
            if '_avanzada' in request.POST:
                return HttpResponseRedirect('/monitoreopf/cruces/')
            
    else:
        form = ConsultarForm()
        request.session['centinela'] = 0

    return render_to_response("monitoreo/consultar.html", RequestContext(request, locals()))

#---------------------------- ACA LAS VISTAS PARA FUNCIONARIOS -------------------------------#
cfunc = ContentType.objects.get(app_label="1-principal", model="funcionario")

# funcion para eliminar opciones que suman 0
verificar = lambda x: sum(x)

def le_hablan_de(request):
    titulo = '¿Cuando alguien le habla de VBG usted cree que estan hablando de?'
    encuestas = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = HablanDe.objects.all()
    for op in opciones:
        tabla[op] = []
    
    for op in opciones:
        for key, grupo in encuestas.items():
            tabla[op].append(ConceptoViolencia.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             hablande=op, respuesta='si').count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def expresion_violencia(request):
    titulo = '¿De que manera considera usted que se expresa la violencia?'
    encuestas = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

    for key, grupo in encuestas.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def comportamiento_funcionario(request):
    from models import CREENCIAS_VBG_RESP
    titulo = u'Como deben comportarse hombres y mujeres'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in Creencia._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            for op in CREENCIAS_VBG_RESP:
                tabla[field.verbose_name][key].append(Creencia.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)

    return render_to_response("monitoreo/funcionarios/comportamiento.html", RequestContext(request, locals()))

def hombres_violentos_func(request):
    titulo = '¿Cree usted que los hombres son violentos debido a?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in CausaVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(CausaVBG.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def hombres_violencia_mujeres_func(request):
    titulo = '¿Cree usted que los hombres son violentos debido a?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in JustificacionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(JustificacionVBG.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/funcionarios/generica_funcionario.html", RequestContext(request, locals()))

def prohibido_por_ley_func(request):
    from models import SI_NO_RESPONDE
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in ConocimientoLey._meta.fields if field.get_internal_type() == 'IntegerField' and not (field.name == 'existe_ley' or field.name == 'object_id')]

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = []

            for op in SI_NO_RESPONDE:    
                tabla[field.verbose_name][key].append(ConocimientoLey.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)
    return render_to_response("monitoreo/funcionarios/prohibido_por_ley_func.html", RequestContext(request, locals()))

def ruta_critica(request):
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    campos = [field for field in RutaCritica._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    opciones = [1, 2, 3, 4, 5]

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = {}

            for op in opciones:
                tabla[field.verbose_name][key][op] = RutaCritica.objects.filter(content_type=cfunc, object_id__in=lista, ** {field.name: op - 1}).count()

    totales = get_total(resultados) 

    totales_vertical = []
    grafico = {}
    for a in range(2):        
        counter = 0
        for i in range(5):
            suma = []
            for key, value in tabla.items():
                for k, v in value.items()[a:a + 1]:
                    suma.append(v.values()[counter])
            counter += 1
            totales_vertical.append(sum(suma))   

    for i in range(5):
        grafico[i + 1] = []

    orden = 0
    for a in range(2):        
        counter2 = 0
        for i in range(5):
            for key, value in tabla.items():
                for k, v in value.items()[a:a + 1]:
                    #calcular el promedio de cada valor
                    promedio = get_prom(v.values()[counter2], totales_vertical[orden])
                    #agregar a la tabla el promedio para cada valor
                    tabla[key][a + 1][i + 1] = [v.values()[counter2], promedio]
                    grafico[i + 1].append({key: v.values()[counter2]})
            counter2 += 1
            orden += 1

    return render_to_response("monitoreo/funcionarios/ruta_critica.html", RequestContext(request, locals()))

def mencione_instrumentos(request):
    titulo = u'¿Mencione algunos de los instrumentos jurídicos que utilizan en la atención a casos de VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = Instrumento.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(RutaCritica.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             instrumentos=op).count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, },
                              RequestContext(request))

def registro_datos(request):
    titulo = u'¿Su institución lleva un registro de datos sobre los casos de VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)
    for key in resultados.keys():
        tabla[key] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for opcion in range(1, 3):
            cantidad = RegistroDato.objects.filter(content_type=cfunc, object_id__in=lista, lleva_registro=opcion).count()
            tabla[key][opcion] = [cantidad, get_prom(cantidad, grupo.count())]

    return render_to_response("monitoreo/funcionarios/generica_pie_func.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def casos_registrados(request):    
    titulo = u'¿Cuántos casos de VBG tienen registrados?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        tabla[key] = RegistroDato.objects.filter(content_type=cfunc, object_id__in=lista).aggregate(casos=Sum('cuantos'))['casos']
    return render_to_response("monitoreo/funcionarios/casos_registrados.html", {'tabla': tabla, 'titulo': titulo, 'totales': totales}, RequestContext(request))

def casos_registrados_por_tipo(request):
    resultados = _query_set_filtrado(request, tipo='funcionario')    
    titulo = u'Qué cantidad de casos de VBG han registrado?'
    campos = [field for field in RegistroDato._meta.fields if field.get_internal_type() == 'IntegerField' and field.name not in ['object_id', 'lleva_registro', 'cuantos']]
    tabla = {}

    for campo in campos:
        tabla[campo.verbose_name] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for campo in campos:
            tabla[campo.verbose_name][key] = RegistroDato.objects.filter(content_type=cfunc, object_id__in=lista).aggregate(cantidad=Sum(campo.name))['cantidad']        

    totales = get_total(resultados)
    return render_to_response("monitoreo/funcionarios/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def calidad_servicios(request):
    from models import SERVICIOS
    titulo = u'¿Cómo valora usted los servicios que su institución ofrece a mujeres que viven VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SERVICIOS:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SERVICIOS:
            tabla[opcion[1]][key] = CalidadAtencionFuncionario.objects.filter(content_type=cfunc, object_id__in=lista, valor_servicio=opcion[0]).count()

    return render_to_response("monitoreo/funcionarios/casos_por_tipo2.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def mejorar_atencion(request):
    from models import SI_NO_SIMPLE2
    titulo = u'¿Ha realizado su institución algunas acciones dirigidas a mejorar la atencion a las mujeres?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SI_NO_SIMPLE2:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SI_NO_SIMPLE2:
            tabla[opcion[1]][key] = AccionMejorarAtencion.objects.filter(content_type=cfunc, object_id__in=lista, realizo_accion=opcion[0]).count()

    return render_to_response("monitoreo/funcionarios/casos_por_tipo2.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def que_acciones(request):    
    titulo = u'¿Cuáles fueron las acciones que su institución realizó?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = Accion.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(AccionMejorarAtencion.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             cuales=op).count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def prevenir_vbg(request):
    from models import SI_NO_SIMPLE2
    titulo = u'¿Su institución realizo algunas acciones dirigidas a prevenir la VBG?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SI_NO_SIMPLE2:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SI_NO_SIMPLE2:
            tabla[opcion[1]][key] = AccionPrevVBG.objects.filter(content_type=cfunc, object_id__in=lista, realizo_accion=opcion[0]).count()
    return render_to_response("monitoreo/funcionarios/casos_por_tipo2.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def cuales_acciones(request):
    titulo = u'¿Cuáles fueron las acciones de prevención de la VBG que su institución realizo?'
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = AccionPrevencion.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(AccionPrevVBG.objects.filter(content_type=cfunc, object_id__in=[encuesta.id for encuesta in grupo], \
                             accion_prevenir=op).count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def donde_buscar_ayuda(request):
    titulo = u'¿Dónde debe buscar ayuda una mujer que vive VBG?'    
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = BuscarAyuda.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]      

        for op in opciones:
            tabla[op].append(AccionVBGFuncionario.objects.filter(content_type=cfunc, object_id__in=lista, donde_buscar=op).count())

    for key, value in tabla.items():
        if verificar(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    
    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))    

def que_debe_hacer_funcionario(request):
    titulo = "¿Si un hombre le pega a su pareja que acciones deberia de tomar?"
    resultados = _query_set_filtrado(request, tipo='funcionario')
    tabla = {}
    opciones = QueDebeHacer.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccionVBGFuncionario.objects.filter(content_type=cfunc, object_id__in=lista, accion_tomar=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def existe_ley_penaliza(request):
    titulo = u'¿Sabe usted si existe alguna ley que penaliza la VBG contra las mujeres?'
    from models import SI_NO_RESPONDE
    resultados = _query_set_filtrado(request, tipo='funcionario')    
    tabla = {}
    
    for op in SI_NO_RESPONDE:
        tabla[op[1]] = []
    
    print tabla

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in SI_NO_RESPONDE:
            tabla[op[1]].append(ConocimientoLey.objects.filter(content_type=cfunc, object_id__in=lista, existe_ley=op[0]).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/funcionarios/generica_pie_func2.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))
    
def recursos_institucion(request):
    titulo = u'¿Con que recursos cuenta su institución para realizar la atención que brinda a las mujeres que viven VBG?'
    resultados = _query_set_filtrado(request, 'funcionario')
    tabla = {}    
    opciones = RecursoCuentaIns.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccionMejorarAtencion.objects.filter(content_type=cfunc, object_id__in=lista, recursos=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/funcionarios/generica_funcionario.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

#obtener la vista adecuada para los indicadores
def _get_view_funcionario(request, vista):
    if vista in VALID_VIEWS_FUNCIONARIO:
        return VALID_VIEWS_FUNCIONARIO[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS_FUNCIONARIO = {
    #vistas para funcionarios, son un turco pero ni moo :S
    'le-hablan-de': le_hablan_de,
    'expresion-violencia': expresion_violencia,
    'comportamiento': comportamiento_funcionario,
    'hombres-violentos-por': hombres_violentos_func,
    'hombres-violencia-mujeres': hombres_violencia_mujeres_func,
    'existe-ley-penaliza': existe_ley_penaliza,
    'prohibido-por-ley': prohibido_por_ley_func,
    'ruta-critica': ruta_critica,
    'registro-datos': registro_datos,
    'casos-registrados': casos_registrados,
    'casos-registrados-por-tipo': casos_registrados_por_tipo,
    'calidad-servicios': calidad_servicios,
    'mejorar-atencion': mejorar_atencion,
    'que-acciones': que_acciones,
    'prevenir-vbg': prevenir_vbg,
    'cuales-acciones': cuales_acciones,
    'mencione-instrumentos': mencione_instrumentos,
    'donde-buscar-ayuda': donde_buscar_ayuda,
    'que-debe-hacer': que_debe_hacer_funcionario,
    'recursos-institucion': recursos_institucion,
}

def get_prom_lista_con_total(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])],
            [value[2], get_prom(value[2], total[2])],
            [value[3], get_prom(value[3], total[3])],
            [value[4], get_prom(value[4], total[4])],
            [value[5], get_prom(value[5], total[5])],
            [value[6], get_prom(value[6], total[6])],
            [value[7], get_prom(value[7], total[7])]]
    return tabla2

def get_prom_lista(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])],
            [value[2], get_prom(value[2], total[2])],
            [value[3], get_prom(value[3], total[3])],
            [value[4], get_prom(value[4], total[4])],
            [value[5], get_prom(value[5], total[5])]]
    return tabla2

def get_prom_lista_func(tabla, total):
    tabla2 = {}
    for key, value in tabla.items():
        tabla2[key] = [[value[0], get_prom(value[0], total[0])],
            [value[1], get_prom(value[1], total[1])]]
    return tabla2

def get_prom_dead_list(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():                        
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key - 1])],
            [value[1], get_prom(value[1], totales[key - 1])],
            [value[2], get_prom(value[2], totales[key - 1])],
            [value[3], get_prom(value[3], totales[key - 1])]]
    return tabla

def get_prom_dead_list2(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key - 1])],
            [value[1], get_prom(value[1], totales[key - 1])],
            [value[2], get_prom(value[2], totales[key - 1])],
            [value[3], get_prom(value[3], totales[key - 1])],
            [value[4], get_prom(value[4], totales[key - 1])]]
    return tabla

def get_prom_dead_list3(tabla, totales):
    for k, v in tabla.items():
        for key, value in v.items():
            tabla[k][key] = [[value[0], get_prom(value[0], totales[key - 1])],
            [value[1], get_prom(value[1], totales[key - 1])]]
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
                dicc[i][j].append(value[i][j - 1])
    return dicc

#------------------------LIDERES Y LIDEREZAS------------------------------------
verificar_dicc = lambda x: x[1] + x[2]

#content type para lider
clider = ContentType.objects.get(app_label="1-principal", model="lider")

def lideres_le_hablan_de(request):
    titulo = '¿Cuando alguien le habla de VBG usted cree que estan hablando de?'
    encuestas = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = HablanDe.objects.all()
    
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in encuestas.items():
            tabla[op].append(ConceptoViolencia.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             hablande=op, respuesta='si').count())
    for key, value in tabla.items():
        if verificar(value) == 0:
            del tabla[key]
    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def expresion_violencia_lideres(request):
    titulo = '¿De que manera considera usted que se expresa la violencia?'
    encuestas = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in ExpresionVBG._meta.fields if field.get_internal_type() == 'CharField']    

    for field in campos:
        tabla[field.verbose_name] = []

    for key, grupo in encuestas.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for field in campos:
            tabla[field.verbose_name].append(ExpresionVBG.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(encuestas)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def comportamiento_lideres(request):
    """Como deben comportarse hombres y mujeres"""
    from models import CREENCIAS_VBG_RESP
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    titulo = 'Como deben comportarse hombres y mujeres'
    campos = [field for field in Creencia._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []           

            for op in CREENCIAS_VBG_RESP:
                tabla[field.verbose_name][key].append(Creencia.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)

    return render_to_response("monitoreo/lideres/comportamiento_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'grafico': grafico, 'totales': totales, 'CREENCIAS_VBG_RESP': CREENCIAS_VBG_RESP},
                              RequestContext(request))

def lideres_hombres_violentos(request):
    titulo = "¿Cree usted que los hombres son violentos debido a?"
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in CausaVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]            

            tabla[field.verbose_name].append(CausaVBG.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def conoce_hombres_violentos(request):
    titulo = u'¿Conoce usted si en su comunidad existen hombres que ejercen VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]       
        
        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=clider, object_id__in=lista, conoce_hombres=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)   

    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def conoce_mujeres_vbg(request):
    titulo = u'¿Conoce usted si en su comunidad existen mujeres que han vivido VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(SituacionVBG.objects.filter(content_type=clider, object_id__in=lista, conoce_mujeres=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def hombres_violencia_mujeres_lideres(request):
    """Para usted, los hombres ejercen violencia hacia las mujeres porque"""
    titulo = u'Para usted, los hombres ejercen violencia hacia las mujeres porque'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in JustificacionVBG._meta.fields if field.get_internal_type() == 'CharField']

    for field in campos:
        tabla[field.verbose_name] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name].append(JustificacionVBG.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: 'si'}).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def ayuda_mujer_violencia_lideres(request):
    """En el ultimo anio ha ayudado usted a alguna mujer que ha vivido VBG"""
    titulo = u'¿En el último año ha ayudado usted a alguna mujer que ha vivido VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, ha_ayudado=op).count())
            
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def donde_buscar_ayuda_lideres(request):
    titulo = '¿Donde debe buscar ayuda una mujer que vive VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = BuscarAyuda.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]      

        for op in opciones:
            tabla[op].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, donde_buscar=op).count())

    for key, value in tabla.items():
        if verificar(value) < 10:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def ha_vivido_vbg(request):
    titulo = u'¿Considera usted que alguna vez ha vivido VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, ha_vivido_vbg=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def mujeres_vbg_comunidad(request):
    from trocaire.encuesta.models import SI_NO_SIMPLE2
    titulo = u'¿Piensa que en su comunidad existen mujeres que han vivido alguna vez VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in SI_NO_SIMPLE2:
        tabla[op[1]] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in SI_NO_SIMPLE2:
            tabla[op[1]].append(PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, piensa_existe=op[0]).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def tipo_vbg_ha_vivido(request):
    resultados = _query_set_filtrado(request, tipo='lider')
    titulo = u'¿Qué tipo de VBG ha vivido?'
    tipos = TipoVBG.objects.all()
    tabla = {}

    for tipo in tipos:
        tabla[tipo] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for tipo in tipos:
            tabla[tipo][key] = PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, que_tipo=tipo).count()

    for key, value in tabla.items():        
        if verificar_dicc(value) == 0:
            del tabla[key]

    totales = get_total(resultados)
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def frecuencia_vbg(request):
    from models import FRECUENCIA
    resultados = _query_set_filtrado(request, tipo='lider')
    titulo = u'¿Con que frecuencia ha vivido situaciones de VBG?'
    tabla = {}

    for tipo in FRECUENCIA:
        tabla[tipo[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for tipo in FRECUENCIA:
            tabla[tipo[1]][key] = PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, frecuencia=tipo[0]).count()

    totales = get_total(resultados)
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def quien_ejercio_vbg(request):
    titulo = u'¿Quién fue la persona que ejecutó esta situación?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    quienes = Quien.objects.all()

    for quien in quienes:
        tabla[quien] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[quien].append(PrevalenciaVBGLider.objects.filter(content_type=clider, object_id__in=lista, quien=quien).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def conocimiento_leyes(request):
    titulo = u'Acciones son prohibidas por la ley'
    from models import SI_NO_RESPONDE
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in ConocimientoLey._meta.fields if field.get_internal_type() == 'IntegerField' and not (field.name == 'existe_ley' or field.name == 'object_id')]

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = []

            for op in SI_NO_RESPONDE:
                tabla[field.verbose_name][key].append(ConocimientoLey.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list(tabla, totales)
    return render_to_response("monitoreo/lideres/prohibido_por_ley.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'grafico': grafico, 'SI_NO_RESPONDE': SI_NO_RESPONDE},
                              RequestContext(request))
    
def existe_ley_penaliza_vbg(request):
    titulo = u'¿Sabe usted si existe alguna ley que penaliza la VBG contra las mujeres?'
    from models import SI_NO_RESPONDE
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    
    for op in SI_NO_RESPONDE:
        tabla[op[1]] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in SI_NO_RESPONDE:
            tabla[op[1]].append(ConocimientoLey.objects.filter(content_type=clider, object_id__in=lista, existe_ley=op[0]).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def decisiones(request):
    titulo = u'¿Cuando una mujer vive VBG cuales acciones deberia realizar?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    quienes = Decision.objects.all()

    for quien in quienes:
        tabla[quien] = []

        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[quien].append(TomaDecision.objects.filter(content_type=clider, object_id__in=lista, decision=quien).count())

    for key, value in tabla.items():
        if verificar(value) < 5:
            del tabla[key]

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def corresponsabilidad(request):
    titulo = u'¿Cuáles de las siguientes actividades realiza usted en su hogar?'
    from models import HOGAR
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in Corresponsabilidad._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]

            tabla[field.verbose_name][key] = []
            for op in HOGAR:
                tabla[field.verbose_name][key].append(Corresponsabilidad.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list2(tabla, totales)
    return render_to_response("monitoreo/lideres/corresponsabilidad.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'grafico': grafico, 'HOGAR': HOGAR},
                              RequestContext(request))

def que_debe_hacer_lideres(request):
    titulo = "¿Si un hombre le pega a su pareja que acciones deberia de tomar?"
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = QueDebeHacer.objects.all()

    for op in opciones:
        tabla[op] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in opciones:
            tabla[op].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, accion_tomar=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def prevenir_vbg_lider(request):
    from models import SI_NO_SIMPLE2
    titulo = u'¿En su organización, escuela o usted realizan algunas acciones dirigidas a prevenir la VBG?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SI_NO_SIMPLE2:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SI_NO_SIMPLE2:
            tabla[opcion[1]][key] = AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, ud_previene=opcion[0]).count()
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def cuales_acciones_lideres(request):
    titulo = u'¿Cuáles fueron las acciones de prevención de la VBG que realizo?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = AccionPrevencion.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(AccionVBGLider.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             accion_prevenir=op).count())
    for key, value in tabla.items():
        if verificar(value) < 5:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, },
                              RequestContext(request))

def mujeres_lideres(request):
    titulo = u'¿Existen mujeres que representan a otras mujeres?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(IncidenciaPolitica.objects.filter(content_type=clider, object_id__in=lista, existen_mujeres=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))
def nivel_satisfaccion(request):
    from models import SATISFECHAS
    titulo = u'¿Qué tan satisfechas están las mujeres con quienes las representan?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    totales = get_total(resultados)

    for opcion in SATISFECHAS:
        tabla[opcion[1]] = {}

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]
        for opcion in SATISFECHAS:
            tabla[opcion[1]][key] = IncidenciaPolitica.objects.filter(content_type=clider, object_id__in=lista, satisfecha=opcion[0]).count()
    return render_to_response("monitoreo/lideres/casos_por_tipo.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def presenta_propuestas(request):
    titulo = u'¿Ha presentado propuestas de acciones de prevención de VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=lista, propuesta=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def tipo_propuesta_presentada(request):
    titulo = u'¿Que tipo de propuesta ha presentado?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = TipoPropuesta.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             si_tipo=op).count())
    for key, value in tabla.items():
        if verificar(value) == 1:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def negocia_propuestas(request):
    titulo = u'¿Ha negociado propuestas de acciones de prevención de VBG?'
    tabla = {}
    resultados = _query_set_filtrado(request, tipo='lider')

    for op in ['si', 'no']:
        tabla[op.title()] = []

    for key, grupo in resultados.items():
        lista = []
        [lista.append(encuesta.id) for encuesta in grupo]

        for op in ['si', 'no']:
            tabla[op.title()].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=lista, propuesta2=op).count())

    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)
    return render_to_response("monitoreo/lideres/generica_lideres_pie.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def tipo_propuesta_negociada(request):
    titulo = u'¿Que tipo de propuesta ha negociado?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = TipoPropuesta.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(CalidadAtencion.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             si_tipo2=op).count())
    for key, value in tabla.items():
        if verificar(value) == 1:
            del tabla[key]
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales, 'nografo': True},
                              RequestContext(request))

def solucion_problema_lideres(request):
    titulo = u'¿Qué se debe hacer para que la solución a un conflicto entre la pareja sea exitoso?'
    from models import DES_AC
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    campos = [field for field in ComunicacionAsertiva._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']
    for field in campos:
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = []
            for op in DES_AC:
                tabla[field.verbose_name][key].append(ComunicacionAsertiva.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op[0]}).count())

    totales = get_total(resultados)
    grafico = convertir_grafico(tabla)
    tabla = get_prom_dead_list3(tabla, totales)

    return render_to_response("monitoreo/lideres/solucion_problema_lideres.html", RequestContext(request, locals()))

def negociacion_exitosa(request):
    titulo = u'¿Qué se debe hacer para que una negociación de pareja sea exitosa?'
    resultados = _query_set_filtrado(request, tipo='lider')
    tabla = {}
    opciones = NegociacionExitosa.objects.all()
    for op in opciones:
        tabla[op] = []

    for op in opciones:
        for key, grupo in resultados.items():
            tabla[op].append(ComunicacionAsertiva.objects.filter(content_type=clider, object_id__in=[encuesta.id for encuesta in grupo], \
                             negociacion_exitosa=op).count())
    totales = get_total(resultados)
    tabla = get_prom_lista_func(tabla, totales)

    return render_to_response("monitoreo/lideres/generica_lideres.html",
                              {'tabla': tabla, 'titulo': titulo, 'totales': totales},
                              RequestContext(request))

def que_hace_ante_vbg(request):
    from trocaire.mujeres_hombres.views import obtener_indice
    resultados = _query_set_filtrado(request, 'lider')
    tabla = {}
    campos = [field for field in AccionVBG._meta.fields if field.get_internal_type() == 'IntegerField' and not field.name == 'object_id']

    opciones = [1, 2, 3, 4, 5, 6]

    for field in campos:        
        tabla[field.verbose_name] = {}
        for key, grupo in resultados.items():
            lista = []
            [lista.append(encuesta.id) for encuesta in grupo]
            tabla[field.verbose_name][key] = {}            
            
            for op in opciones:
                tabla[field.verbose_name][key][op] = AccionVBGLider.objects.filter(content_type=clider, object_id__in=lista, ** {field.name: op - 1}).count()
    totales = get_total(resultados)
    
    #---------------Inicia transformacion para grafico ------------------------
    grafico = {}
    for key, value in tabla.items():
        grafico[key] = {}
        for i in range(1, 3):
            grafico[key][i] = obtener_indice(tabla[key][i])
            
    return render_to_response("monitoreo/lideres/que_hace_ante_vbg.html", RequestContext(request, locals()))

def _get_vista_lideres(request, vista):
    if vista in VALID_VIEWS_LIDERES:
        return VALID_VIEWS_LIDERES[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS_LIDERES = {
    'le-hablan-de': lideres_le_hablan_de,
    'hombres-violentos': lideres_hombres_violentos,
    'comportamiento': comportamiento_lideres,
    'justificacion': hombres_violencia_mujeres_lideres,
    'ayuda-mujer': ayuda_mujer_violencia_lideres,
    'donde-buscar-ayuda': donde_buscar_ayuda_lideres,
    'expresion-violencia': expresion_violencia_lideres,
    'conoce-hombres-violentos': conoce_hombres_violentos,
    'conoce-mujeres-vbg': conoce_mujeres_vbg,
    'mujeres-vbg-comunidad': mujeres_vbg_comunidad,
    'ha-vivido-vbg': ha_vivido_vbg,
    'tipo-vbg-ha-vivido': tipo_vbg_ha_vivido,
    'frecuencia-vbg': frecuencia_vbg,
    'quien-ejercio-vbg': quien_ejercio_vbg,
    'prohibido-por-ley': conocimiento_leyes,
    'existe-ley-penaliza-vbg': existe_ley_penaliza_vbg,
    'decisiones': decisiones,
    'corresponsabilidad': corresponsabilidad,
    #aca la tabla fea
    'que-debe-hacer': que_debe_hacer_lideres,
    'prevenir-vbg': prevenir_vbg_lider,
    'cuales-acciones': cuales_acciones_lideres,
    'mujeres-lideres': mujeres_lideres,
    'nivel-satisfaccion': nivel_satisfaccion,
    'presenta-propuestas': presenta_propuestas,
    'negocia-propuestas': negocia_propuestas,
    'tipo-propuesta-presentada': tipo_propuesta_presentada,
    'tipo-propuesta-negociada': tipo_propuesta_negociada,
    'solucion-problema-lideres': solucion_problema_lideres,
    'negociacion-exitosa': negociacion_exitosa,
    'que-hace-ante-vbg': que_hace_ante_vbg,
}
