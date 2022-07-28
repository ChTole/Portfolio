from django.urls import path
from . import views

urlpatterns = [
    path('detalle-curso/<tema_id>', views.detalle_curso, name="detalle-curso"),
    path('cursos-disponibles', views.cursos_disponibles, name="cursos-disponibles"),
    path('detalle-comision/<nro_comision>', views.detalle_comision, name="detalle-comision"),
]