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
    