from django.db import models

# Create your models here.
class Transaccion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.fecha} - {self.descripcion} - {self.monto} - {self.tipo}"