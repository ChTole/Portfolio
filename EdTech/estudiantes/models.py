from django.db import models
from django.contrib import messages

from usuarios.models import Usuario
from cursos.models import Comision


class CursoInscripto(models.Model):
    curso_inscripto = models.ForeignKey(Comision, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Estudiantes"})
        
    def __str__(self):
        return f"{self.estudiante} - {self.curso_inscripto}"
        
    def save(self, *args, **kwargs):
        inscriptos = CursoInscripto.objects.filter(curso_inscripto=self.curso_inscripto)
        if inscriptos.filter(estudiante=self.estudiante):
            # ver messages
            return print("no se grabó!!!")
        vacantes = self.curso_inscripto.vacantes
        if inscriptos and vacantes:
            if inscriptos.count() >= vacantes:
                # ver messages
                return print("no se grabó!!!")
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Estudiantes inscriptos'
