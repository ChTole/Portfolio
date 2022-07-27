from django.urls import path
from . import views

urlpatterns = [
    path('estudiante', views.estudiante, name="estudiantes_inicio"),
    path('inscripcion/<curso_id>', views.inscribir_curso, name="inscribir-curso"),
]