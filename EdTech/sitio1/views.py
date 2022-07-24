from django.shortcuts import render

from cursos.models import Tema

def inicio(request):
    cursos = Tema.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "sitio1/inicio.html", ctx)