from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
# def index(request):
#     return HttpResponse("<h1>Probando sitio FORO-MENSAJERIA</h1>")

class ForoList(ListView):
    model = Posteo
    template_name = "foro/foro.html"
    paginate_by = 5
    
    class Meta: 
        ordering = ['fecha']
    
class ForoDetail(DetailView):
    model = Posteo
    template_name = "foro/posteo.html"