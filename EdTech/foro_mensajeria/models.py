from distutils.command.upload import upload
import imp
from django.db import models

from usuarios.models import Usuario

class Posteo(models.Model):
    tema = models.CharField("Tema", max_length=20, unique=True)
    titulo = models.CharField("Título", max_length=50)
    fecha = models.DateField("Fecha", auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField("Contenido", max_length=200)
    imagen = models.ImageField(upload_to='media/foro', null=True, blank=True)
    
class Comentario(models.Model):
    posteo_rel = models.ForeignKey(Posteo, on_delete=models.CASCADE)
    fecha = models.DateField("Fecha", auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField("Contenido", max_length=200)
    imagen = models.ImageField(upload_to='media/foro', null=True, blank=True)
    
class Mensaje(models.Model):
    fecha = models.DateField("Fecha", auto_now=True)
    autor = models.ForeignKey(Usuario, related_name='autor', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Usuario, related_name='destinatario', on_delete=models.CASCADE)
    comentario = models.TextField("Contenido", max_length=200)
    imagen = models.ImageField(upload_to='media/foro', null=True, blank=True)