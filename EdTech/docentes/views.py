from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import CursoPostulado
from cursos.models import Comision

@login_required
def docentes(request):
    postulaciones = CursoPostulado.objects.filter(docente=request.user)
    ctx = {"postulaciones": postulaciones}
    return render(request, "docentes/docentes_inicio.html", ctx)

