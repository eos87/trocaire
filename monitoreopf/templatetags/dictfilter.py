from django import template
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
def ordenar(value):
    dicc = sorted(value.items(), key=lambda x: x[1], reverse=True)
    return dicc 
