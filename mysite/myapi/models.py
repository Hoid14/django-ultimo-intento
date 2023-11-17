from django.db import models
from django.utils import timezone
# Create your models here.
class Finanzas(models.Model):
    titulo = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo