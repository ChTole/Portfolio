from django.shortcuts import render

from cursos.models import Tema

def index(request):
    cursos = Tema.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "sitio1/index.html", ctx)