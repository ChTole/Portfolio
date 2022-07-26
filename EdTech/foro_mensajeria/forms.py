from django import forms

from .models import Mensaje, Comentario

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido', 'imagen']
        
class ComentarioForm(forms.ModelForm):
    class  Meta:
        model = Comentario
        fields = ['comentario', 'imagen']