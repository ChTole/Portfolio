from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

def detalle_curso(request, tema_id):
    tema = Tema.objects.get(id = tema_id)
    comisiones = Comision.objects.filter(tema_curso = tema)
    ctx = {"tema": tema, "comisiones": comisiones}
    return render(request, "cursos/detalle_curso.html", ctx)

@login_required
def cursos_disponibles(request):
    disponibles = Comision.objects.all() 
    ctx = {"disponibles": disponibles}
    return render(request, "cursos/cursos_disp.html", ctx)

