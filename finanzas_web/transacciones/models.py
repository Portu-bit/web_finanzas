from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Transaccion(models.Model):
    class Tipo(models.TextChoices):
        INGRESO = "ingreso", "Ingreso"
        GASTO = "gasto", "Gasto"

    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])
    tipo = models.CharField(max_length=10, choices=Tipo.choices)

    def __str__(self):
        return f"{self.fecha:%Y-%m-%d %H:%M} - {self.get_tipo_display()} - {self.descripcion} - {self.monto}"
