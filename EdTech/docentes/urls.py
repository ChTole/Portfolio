from django.urls import path
from . import views

urlpatterns = [
    path('docente', views.docentes, name="docentes_inicio"),
    path('cursos-disponibles', views.cursos_disponibles, name="cursos-disponibles"),
]