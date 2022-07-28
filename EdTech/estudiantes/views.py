from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cursos.models import Comision
from .models import CursoInscripto

@login_required
def estudiante(request):
    cursos = CursoInscripto.objects.filter(estudiante=request.user)
    ctx = {"cursos": cursos}
    return render(request, "estudiantes/estudiantes_inicio.html", ctx)

@login_required
def inscribir_curso(request, curso_id):
    curso = Comision.objects.get(id = curso_id)
    if request.method == "POST":
        estudiante_i = request.user
        CursoInscripto.objects.create(curso_inscripto = curso, estudiante = estudiante_i)
        return redirect('inicio')
    ctx = {"curso": curso}
    return render(request, "estudiantes/inscripcion.html", ctx)