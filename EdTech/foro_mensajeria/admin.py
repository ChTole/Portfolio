from django.contrib import admin

from .models import *

admin.site.register(Posteo)
admin.site.register(Comentario)
admin.site.register(Mensaje)