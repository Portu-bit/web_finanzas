from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("transacciones", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="transaccion",
            name="monto",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[MinValueValidator(Decimal("0.01"))],
            ),
        ),
        migrations.AlterField(
            model_name="transaccion",
            name="tipo",
            field=models.CharField(
                choices=[("ingreso", "Ingreso"), ("gasto", "Gasto")],
                max_length=10,
            ),
        ),
    ]
