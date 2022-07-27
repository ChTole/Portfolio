from django.urls import path
from . import views

urlpatterns = [
    path('docente', views.docentes, name="docentes_inicio"),
    path('postulacion/<curso_id>', views.postular_curso, name="postular"),
]