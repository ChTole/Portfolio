from django.urls import path
from . import views

urlpatterns = [
    path('estudiante', views.index, name="estudiantes_inicio"),
]