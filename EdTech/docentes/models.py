from django.db import models

from usuarios.models import Usuario
from cursos.models import Comision

class CursoPostulado(models.Model):
    curso_postulado = models.ForeignKey(Comision, on_delete=models.CASCADE)
    docente = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Docentes"})
        
    def __str__(self):
        return f"{self.docente} - {self.curso_postulado}"
    
    class Meta:
        verbose_name_plural = 'Postulaciones a Cursos'