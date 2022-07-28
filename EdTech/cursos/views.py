from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from docentes.models import CursoPostulado
from estudiantes.models import CursoInscripto

def detalle_curso(request, tema_id):
    tema = Tema.objects.get(id = tema_id)
    comisiones = Comision.objects.filter(tema_curso = tema)
    ctx = {"tema": tema, "comisiones": comisiones}
    return render(request, "cursos/detalle_curso.html", ctx)


@login_required
def cursos_disponibles(request):
    if request.user.tipo_usuario == 1:
        inscr_post = CursoInscripto
        postulaciones = inscr_post.objects.filter(estudiante=request.user)
    elif request.user.tipo_usuario == 2:
        inscr_post = CursoPostulado
        postulaciones = inscr_post.objects.filter(docente=request.user)
    cursos = Comision.objects.all()
    no_disponibles = []
    for curso in cursos:
        for postulados in inscr_post.objects.all():
            if curso.nro_comision == postulados.curso_postulado.nro_comision:
                no_disponibles.append(curso.nro_comision)
    ctx = {
        "cursos": cursos,
        "postulaciones": postulaciones,
        "no_disponibles": no_disponibles,
    }
    return render(request, "cursos/cursos_disp.html", ctx)

@login_required
def detalle_comision(request, nro_comision):
    curso = Comision.objects.get(nro_comision = nro_comision)
    estudiantes = CursoInscripto.objects.filter(curso_inscripto = curso.id)
    print(estudiantes)
    ctx = {
        "curso": curso,
        "estudiantes": estudiantes,
    }
    return render(request, "cursos/detalle_comision.html", ctx)