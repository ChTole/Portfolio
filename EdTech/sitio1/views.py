from django.shortcuts import render
from django.db.models import Q

from cursos.models import Tema
from estudiantes.models import CursoInscripto

def inicio(request):
    if request.user.is_authenticated:
        inscriptos = CursoInscripto.objects.filter(estudiante = request.user)
        if inscriptos:
            no_disp = Q()
            for inscripto in inscriptos:
                no_disp_curso = Tema.objects.get(tema = inscripto.curso_inscripto.tema_curso.tema)
                if no_disp_curso:
                    no_disp.add((~Q(tema = inscripto.curso_inscripto.tema_curso.tema)), Q.AND)
            cursos = Tema.objects.filter(no_disp)
        else:
            cursos = Tema.objects.all()
    else:
        cursos = Tema.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "sitio1/inicio.html", ctx)