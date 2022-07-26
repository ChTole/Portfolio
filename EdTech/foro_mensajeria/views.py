from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

class ForoList(LoginRequiredMixin, ListView):
    model = Posteo
    template_name = "foro/foro.html"
    paginate_by = 5
    
    class Meta: 
        ordering = ['fecha']
    
class ForoDetail(LoginRequiredMixin, DetailView):
    model = Posteo
    template_name = "foro/posteo.html"
    
class MensajesRecibidosList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'comunicacion/mensajes_recibidos.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(destinatario = self.request.user)

class MensajesEnviadosList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'comunicacion/mensajes_enviados.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(autor = self.request.user)
    
class MensajeDetail(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'comunicacion/mensaje_detail.html'
    fields = '__all__'
    
@login_required
def nuevo_mensaje(request):
    if request.method == "POST":
        form =  MensajeForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit = False)
            nuevo_mensaje.autor = request.user
            nuevo_mensaje.save()
            return redirect('mensajes-enviados')
    else:
        form = MensajeForm()
    ctx = {"form": form}
    return render(request, "comunicacion/nuevo_mensaje.html", ctx)

@login_required
def reenviar_responder(request, mensaje_id):
    mensaje = Mensaje.objects.get(id = mensaje_id)
    if request.method == "POST":
        form =  MensajeForm(request.POST, instance = mensaje)
        if form.is_valid():
            nuevo_mensaje = form.save(commit = False)
            nuevo_mensaje.autor = request.user
            nuevo_mensaje.save()
            return redirect('mensajes-enviados')
    else:
        form = MensajeForm(instance = mensaje)
    ctx = {"form": form}
    return render(request, "comunicacion/nuevo_mensaje.html", ctx)