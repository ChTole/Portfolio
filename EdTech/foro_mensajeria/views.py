from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Foro

class ForoList(LoginRequiredMixin, ListView):
    model = Posteo
    template_name = "foro/foro.html"
    paginate_by = 3
    ordering = ['-fecha']
              
def posteo_detalle(request, posteo_id):
    posteo = Posteo.objects.get(id = posteo_id)
    comentario = ComentarioForm(request.POST, request.FILES)
    if request.method == "POST":
        if comentario.is_valid():
            nuevo_comentario = comentario.save(commit = False)
            nuevo_comentario.posteo_rel = posteo
            nuevo_comentario.autor = request.user
            nuevo_comentario.save()
            return redirect(f'../posteo/{posteo_id}' )
    ctx = {
        "posteo": posteo,
        "form": comentario
    }
    return render(request, "foro/posteo.html", ctx)

class ForoCreate(LoginRequiredMixin, CreateView):
    model = Posteo
    template_name = "foro/nuevo_post.html"
    success_url = "foro/list"
    fields = ('tema', 'titulo', 'contenido', 'imagen')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Mensajería

class MensajesRecibidosList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'comunicacion/mensajes_recibidos.html'
    paginate_by = 5
    ordering = ['-fecha']

    def get_queryset(self):
        return self.model.objects.filter(destinatario = self.request.user)

class MensajesEnviadosList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'comunicacion/mensajes_enviados.html'
    paginate_by = 5
    ordering = ['-fecha']

    def get_queryset(self):
        return self.model.objects.filter(autor = self.request.user)
    
class MensajeDetail(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'comunicacion/mensaje_detail.html'
    fields = '__all__'
    
@login_required
def nuevo_mensaje(request):
    if request.method == "POST":
        form =  MensajeForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_mensaje = form.save(commit = False)
            nuevo_mensaje.autor = request.user
            nuevo_mensaje.save()
            return redirect('mensajes-enviados')
    else:
        form = MensajeForm()
    ctx = {
        "titulo": "Nuevo mensaje",
        "form": form,
    }
    return render(request, "comunicacion/nuevo_mensaje.html", ctx)

@login_required
def reenviar_responder(request, mensaje_id):
    mensaje = Mensaje.objects.get(id = mensaje_id)
    initial_data = {
        "autor": request.user,
        "asunto": f"Re/Rv: {mensaje.asunto}",
        "contenido": f"El {mensaje.fecha}, {mensaje.autor} escribió: {mensaje.contenido}",
        "imagen": mensaje.imagen,
    }
    if request.method == "POST":
        form =  MensajeForm(request.POST, request.FILES, initial = initial_data)
        if form.is_valid():
            nuevo_mensaje = form.save(commit = False)
            nuevo_mensaje.autor = request.user
            nuevo_mensaje.save()
            return redirect('mensajes-enviados')
    else:
        form = MensajeForm(initial = initial_data)
    ctx = {
        "titulo": "Reenviar/Responder",
        "form": form,
    }
    return render(request, "comunicacion/nuevo_mensaje.html", ctx)