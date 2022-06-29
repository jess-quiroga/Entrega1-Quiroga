from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('actividades', views.actividades, name="Actividades"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesores', views.profesores, name="Profesores"),
    path('patrocinadores', views.patrocinadores, name="Patrocinadores"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
]