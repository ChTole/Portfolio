from django.shortcuts import render

from .models import *

def detalle_curso(request, tema_id):
    tema = Tema.objects.get(id = tema_id)
    comisiones = Comision.objects.filter(tema_curso = tema)
    ctx = {"tema": tema, "comisiones": comisiones}
    return render(request, "cursos/detalle_curso.html", ctx)
