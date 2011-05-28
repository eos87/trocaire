# -*- coding: UTF-8 -*-
from django import forms

VARIABLE_MUJER_1 = ((1, u'Nivel Educativo'),
				(2, u'Trabajo'),
				(3, u'Número de hijos'),
				(4, u'Si Estudia'),
				(5, u'Estado civil'))

VARIABLE_MUJER_2 = ((1, u'¿Alguna vez ha vivido violencia?'), 
			(2, u'¿Qué tipo de VBG ha vivido?'),
            (3, u'¿Con que frecuencia ha vivido VBG?'),
            (4, u'¿Quién es la persona que ha ejercido VBG sobre usted?'),            
            (5, u'¿Cómo valora los servicios de las instituciones para mujeres que viven VBG?'),
            (6, u'¿Cómo afecta la VBG a las mujeres, la familia y comunidad?'))

class MujerCrucesForm(forms.Form):
	variable_1 = forms.ChoiceField(choices=VARIABLE_MUJER_1, label=u'Variable 1', widget=forms.RadioSelect)
	variable_2 = forms.ChoiceField(choices=VARIABLE_MUJER_2, label=u'Variable 2', widget=forms.RadioSelect)


VARIABLE_HOMBRE_1 = ((6, u'Nivel Educativo'),
				(7, u'Trabajo'),
				(8, u'Estado civil'))

VARIABLE_HOMBRE_2 = ((7, u'¿Alguna vez ha ejercido violencia?'), 
			(8, u'¿Qué tipo de VBG ha ejercido?'),
            (9, u'¿Con que frecuencia ha ejercido VBG?'),
            (10, u'¿Qué parentezco tiene con la persona contra la que Ud ejerció VBG?'),
            (11, u'¿Cómo afecta la VBG a las mujeres, la familia y comunidad?'))

class HombreCrucesForm(forms.Form):
	variable_hombre_1 = forms.ChoiceField(choices=VARIABLE_HOMBRE_1, label=u'Variable 1', widget=forms.RadioSelect)
	variable_hombre_2 = forms.ChoiceField(choices=VARIABLE_HOMBRE_2, label=u'Variable 2', widget=forms.RadioSelect)
	
	