# -*- coding: UTF-8 -*-
from django import forms
from trocaire.lugar.models import Pais, Departamento, Municipio
from models import Mujer, Contraparte

NIVEL_EDUCATIVO = (('', 'Todos'), 
			('primaria-completa', 'Primaria Completa'),
            ('primaria-incompleta', 'Primaria Incompleta'),
            ('secundaria-completa', 'Secundaria Completa'),
            ('secundaria-incompleta', 'Secundaria Incompleta'),
            ('tecnico', 'Técnico o Tecnólogo'),
            ('universitario-sin-titulo', 'Universitario sin título'),
            ('universitario-con-titulo', 'Universitario con título'),
            ('postgrado', 'Postgrado'),
            ('ninguno', 'Ninguno'))

IGLESIA = (('', 'Todo'), (1, 'Si'), (2, 'No'))
			
#mostrar solo los años donde hay informacion en BD
def get_anios():
    choices = []
    years = []
    for en in Mujer.objects.all().order_by('fecha'):
        years.append(en.fecha.year)
    for year in list(set(years)):
        choices.append((year, year))
    return choices

class ConsultarForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		super(ConsultarForm, self).__init__(*args, **kwargs)
		self.fields['year'].choices = get_anios()

	year = forms.ChoiceField(choices=get_anios(), label=u'Año')
	nivel_educativo = forms.ChoiceField(choices=NIVEL_EDUCATIVO, required=False)
	iglesia = forms.ChoiceField(choices=IGLESIA, required=False)
	pais = forms.ModelMultipleChoiceField(queryset=Pais.objects.all(), required=False)
	departamento = forms.ModelMultipleChoiceField(queryset=Departamento.objects.all(), required=False, label=u'Departamento/Provincia')
	organizacion = forms.ModelMultipleChoiceField(queryset=Contraparte.objects.all(), required=False)
	municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all(), required=False, label=u'Municipio/Cantón')
	
	