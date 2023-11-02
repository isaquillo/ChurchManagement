from django.db import models
from personas.models import Persona

# Create your models here.


class Celula(models.Model):

    DIAS_SEMANA = [
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miercoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
        ('SABADO', 'Sabado'),
        ('DOMINGO', 'Domingo')
    ]

    nombre = models.CharField(max_length=100, null=False)
    lider = models.ForeignKey(
        Persona, null=True, on_delete=models.SET_NULL, related_name='lider', default=None)
    auxiliar = models.ForeignKey(
        Persona, null=True, on_delete=models.SET_NULL, related_name='auxiliar', default=None)
    anfitrion = models.ForeignKey(
        Persona, null=True, on_delete=models.SET_NULL, related_name='anfitrion', default=None)
    ubicacion = models.CharField(max_length=200, null=False)
    dia_de_reunion = models.CharField(
        choices=DIAS_SEMANA, max_length=10, null=True, blank=True, default='')
    hora_reunion = models.TimeField(null=True, blank=True, default='')
    descripcion = models.TextField(null=True, blank=True, default='')

    def __str__(self) -> str:
        return 'Célula: ' + self.nombre + ',' + ' Lider: ' + self.lider.nombre + ',' + ' Ubicacion: ' + self.ubicacion
