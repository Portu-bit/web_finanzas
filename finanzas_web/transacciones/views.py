from decimal import Decimal
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .forms import TransaccionForm
from .models import Transaccion


def transacciones_list(request):
    transacciones = Transaccion.objects.all()
    totales = Transaccion.objects.values("tipo").annotate(total=Sum("monto"))
    resumen = {item["tipo"]: item["total"] or Decimal("0.00") for item in totales}
    ingresos = resumen.get(Transaccion.Tipo.INGRESO, Decimal("0.00"))
    gastos = resumen.get(Transaccion.Tipo.GASTO, Decimal("0.00"))
    return render(request, "transacciones/transacciones_list.html", {
        "transacciones": transacciones,
        "total_ingresos": ingresos,
        "total_gastos": gastos,
        "balance": ingresos - gastos,
    })


@require_http_methods(["GET", "POST"])
def agregar_transaccion(request):
    if request.method == "POST":
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La transacción se guardó correctamente.")
            return redirect("lista_transacciones")
        messages.error(request, "Revisa los errores del formulario.")
    else:
        form = TransaccionForm()
    return render(request, "transacciones/agregar.html", {"form": form})
