from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.
def actividades(request):

      actividades =  Actividades(nombre="Fútbol", profesor="Carlos Magno", sede= "Córdoba centro")
      actividades.save()
      documentoDeTexto = f"--->Actividades: {actividades.nombre}   Profesor: {actividades.profesor}   Sede: {actividades.sede}"

      return HttpResponse(documentoDeTexto)

def estudiantes(request):

      estudiantes =  Estudiantes(nombre="Martin", apellido="Salguero", DNI= 40895745, disciplina= "Fútbol")
      estudiantes.save()
      documentoDeTexto = f"--->Estudiantes: {estudiantes.nombre}   Apellido: {estudiantes.apellido}   DNI: {estudiantes.DNI}   Disciplina: {estudiantes.disciplina}"

      return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def actividades(request):
    return render(request, "AppCoder/actividades.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def patrocinadores(request):
    return render(request, "AppCoder/patrocinadores.html")
    

def actividadesFormulario(request):

      if request.method == 'POST':

            miFormulario = actividadesFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  actividades = Actividades (nombre=informacion['actividades'], profesor=informacion['profesor'], sede=informacion['sede'] ) 

                  actividades.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= actividadesFormulario()

      return render(request, "AppCoder/actividades.html", {"miFormulario":miFormulario})



def estudiantes(request):

      if request.method == 'POST':

            miFormulario = estudiantesFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid: 

                  informacion = miFormulario.cleaned_data

                  estudiantes = Estudiantes (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   DNI=informacion['dni'], disciplina=informacion['disciplina']) 

                  estudiantes.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= estudiantesFormulario() 

      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})

def profesores(request):

      if request.method == 'POST':

            miFormulario = profesoresFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid: 

                  informacion = miFormulario.cleaned_data

                  profesores = Profesores (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   DNI=informacion['dni'], disciplina=informacion['disciplina']) 

                  profesores.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= profesoresFormulario() 

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})


def patrocinadoresFormulario(request):

      if request.method == 'POST':

            miFormulario = patrocinadoresFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  patrocinadores = Patrocinadores (nombre=informacion['actividades'], rubro=informacion['rubro'], telefono=informacion['telefono'] ) 

                  actividades.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= patrocinadoresFormulario()

      return render(request, "AppCoder/actividades.html", {"miFormulario":miFormulario})
