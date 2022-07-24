from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import *

class ForoList(LoginRequiredMixin, ListView):
    model = Posteo
    template_name = "foro/foro.html"
    paginate_by = 5
    
    class Meta: 
        ordering = ['fecha']
    
class ForoDetail(LoginRequiredMixin, DetailView):
    model = Posteo
    template_name = "foro/posteo.html"
    
@login_required
def mensajes(request):
    recibidos = Mensaje.objects.filter(destinatario = request.user)
    enviados = Mensaje.objects.filter(autor = request.user)
    ctx = {"enviados": enviados, "recibidos": recibidos}
    return render(request, "comunicacion/mensajes.html", ctx)