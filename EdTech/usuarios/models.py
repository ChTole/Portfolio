from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    dni = models.PositiveIntegerField(
        "Documento de identidad", 
        unique=True,  
        validators=[
            MaxValueValidator(99999999),
            MinValueValidator(1000000)
            ])
    TIPO = (
        (1, 'Estudiante'),
        (2, 'Docente'),
        (3, 'Personal N1'),
        (4, 'Personal N2'),
        (5, 'Personal N3'),
        (6, 'Backend'),
    )
    tipo_usuario = models.PositiveSmallIntegerField("Tipo",choices=TIPO, null=True)
    avatar = models.ImageField(upload_to='avatares', null = True, blank = True)
    username = None
    
    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['first_name','last_name', 'email']
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_tipo_usuario_display()}"