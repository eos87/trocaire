from django import template
from trocaire.utils import get_prom
register = template.Library()

@register.filter
def dict_get(value, arg):
    """custom template tag used like so:
    {{dictionary|dict_get:var}}
    where dictionary is duh a dictionary and var is a variable representing
    one of it's keys"""

    return value[arg]

@register.filter
def sumar(value, arg):    

    return value + arg

@register.filter
def ordenar(dicc, arg):
    value = dict.copy(dicc)
    for k, v in value.items():                        
        value[k] = get_prom(value[k], arg[k])        
    dicc = sorted(value.items(), key=lambda x: x[1], reverse=True)
    return dicc

@register.filter
def get_promedio(value, arg):    
    return get_prom(value, arg)