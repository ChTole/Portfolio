from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Tema(models.Model):
    tema = models.CharField("Título curso", max_length=50, unique=True)
    imagen = models.ImageField("Logo", upload_to='cursos_logos', null=True, blank=True)        
    
    def __str__(self):
        return f"{self.tema}"

class Comision(models.Model):
    tema_curso = models.ForeignKey(Tema, on_delete=models.CASCADE)
    nro_comision = models.PositiveIntegerField("Comisión Nro.", unique=True)
    vacantes = models.PositiveSmallIntegerField("Vacantes", validators=[MaxValueValidator(10)])
    inicio = models.DateField("Inicio", null=True)
    final = models.DateField("Final", null=True)
    
    def __str__(self):
        return f"{self.tema_curso} - [{self.nro_comision}] - Vacantes: {self.vacantes} - Desde: {self.inicio} hasta: {self.final}"
    
    class Meta:
        verbose_name_plural = 'Comisiones'