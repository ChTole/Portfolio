from django.urls import path
from . import views

urlpatterns = [
    path('docente/<user_id>', views.docentes, name="docentes_inicio"),
    path('cursos-disponibles/', views.cursos_disponibles, name="cursos-disponible"),
]