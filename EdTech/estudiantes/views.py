from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import CursoInscripto

@login_required
def estudiante(request):
    cursos = CursoInscripto.objects.filter(estudiante=request.user)
    ctx = {"cursos": cursos}
    return render(request, "estudiantes/estudiantes_inicio.html", ctx)