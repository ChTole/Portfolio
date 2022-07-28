from django import forms
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Usuario

class UsuarioCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    dni = forms.IntegerField(label="Documento")
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña:', widget=forms.PasswordInput)
        
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'dni', 'email', 'password1', 'password2']
        # Quita mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
class UsuarioEditForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'avatar', 'password1', 'password2']
        # Quita mensajes de ayuda
        help_texts = {k:"" for k in fields}