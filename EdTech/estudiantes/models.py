from django.db import models
from django.contrib import messages

from usuarios.models import Usuario
from cursos.models import Comision


class CursoInscripto(models.Model):
    curso_inscripto = models.ForeignKey(Comision, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)#, limit_choices_to={'groups__name': "Estudiantes"})
        
    def __str__(self):
        return f"{self.estudiante} - {self.curso_inscripto}"
        
    def save(self, *args, **kwargs):
        inscriptos = CursoInscripto.objects.filter(curso_inscripto=self.curso_inscripto).count()
        vacantes = Comision.objects.get(curso=self.curso_inscripto).vacantes
        print(inscriptos, vacantes)
        if inscriptos and vacantes:
            if inscriptos >= vacantes:
                return messages.error("Las vacantes para el curso estan completas o aún no se han habilitado!")
        super().save(*args, **kwargs)
