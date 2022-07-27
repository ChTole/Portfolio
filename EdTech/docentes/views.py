from django.shortcuts import redirect, render
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
    cursos = Comision.objects.all()
    postulaciones = CursoPostulado.objects.filter(docente=request.user)
    no_disponibles = []
    for curso in cursos:
        for postulados in CursoPostulado.objects.all():
            if curso.nro_comision == postulados.curso_postulado.nro_comision:
                no_disponibles.append(curso.nro_comision)
    ctx = {
        "cursos": cursos,
        "postulaciones": postulaciones,
        "no_disponibles": no_disponibles,
    }
    return render(request, "docentes/cursos_disp.html", ctx)

def postular_curso(request, curso_id):
    curso = Comision.objects.get(id = curso_id)
    if request.method == "POST":
        docente_p = request.user
        CursoPostulado.objects.create(curso_postulado = curso, docente = docente_p)
        return redirect('cursos-disponibles')
    ctx = {"curso": curso}
    return render(request, "docentes/postulacion.html", ctx)