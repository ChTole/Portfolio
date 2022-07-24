from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import CursoPostulado
from cursos.models import Comision

@login_required
def docentes(request):
    postulaciones = CursoPostulado.objects.filter(docente=request.user)
    ctx = {"postulaciones": postulaciones}
    return render(request, "docentes/docentes_inicio.html", ctx)

@login_required
def cursos_disponibles(request):
    disponibles = Comision.objects.all() 
    ctx = {"disponibles": disponibles}
    return render(request, "docentes/cursos_disp.html", ctx)