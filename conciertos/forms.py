from django import forms

from .models import Grupo, Musico, Concierto


class GrupoForm(forms.Form):
    nombre = forms.CharField()
    estilo = forms.CharField()

class MusicoForm(forms.Form):
    nombre = forms.CharField()
    instrumento = forms.CharField()
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all())    

class ConciertoForm(forms.Form):
    fecha = forms.DateTimeField(widget=forms.SelectDateWidget())
    lugar = forms.CharField()
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all())    

