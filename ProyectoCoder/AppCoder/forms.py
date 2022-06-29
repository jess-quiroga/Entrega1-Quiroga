from django import forms


class ActividadesFormulario(forms.Form):
    nombre= forms.CharField
    profesor=forms.CharField
    sede=forms.CharField

class EstudiantesFormulario(forms.Form):
    nombre= forms.CharField
    apellido= forms.CharField
    DNI= forms.IntegerField
    disciplina= forms.CharField

class ProfesoresFormulario(forms.Form):
    nombre= forms.CharField
    apellido= forms.CharField
    DNI= forms.IntegerField
    disciplina= forms.CharField

class PatrocinadoresFormulario(forms.Form):
    nombre= forms.CharField
    rubro= forms.CharField
    telefono= forms.IntegerField
