from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import CursoPostulado
from cursos.models import Comision

@login_required
def docentes(request, user_id):
    postulaciones = CursoPostulado.objects.filter(docente=user_id)
    ctx = {"postulaciones": postulaciones}
    return render(request, "docentes/docentes_inicio.html", ctx)

@login_required
def cursos_disponibles(request):
    disponibles = Comision.objects.all() 
    ctx = {"disponibles": disponibles}
    return render(request, "docentes/cursos_disp.html", ctx)