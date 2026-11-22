from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from .models import Transaccion


class TransaccionesViewsTests(TestCase):
    def test_list_page_loads(self):
        response = self.client.get(reverse("lista_transacciones"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista de transacciones")

    def test_create_income(self):
        response = self.client.post(reverse("agregar_transaccion"), {
            "tipo": Transaccion.Tipo.INGRESO, "descripcion": "Salario", "monto": "1500.00",
        })
        self.assertRedirects(response, reverse("lista_transacciones"))
        self.assertEqual(Transaccion.objects.get().monto, Decimal("1500.00"))

    def test_create_expense(self):
        response = self.client.post(reverse("agregar_transaccion"), {
            "tipo": Transaccion.Tipo.GASTO, "descripcion": "Comida", "monto": "25.50",
        })
        self.assertRedirects(response, reverse("lista_transacciones"))
        self.assertEqual(Transaccion.objects.get().tipo, Transaccion.Tipo.GASTO)

    def test_reject_zero_or_negative_amount(self):
        for amount in ("0", "-1.00"):
            response = self.client.post(reverse("agregar_transaccion"), {
                "tipo": Transaccion.Tipo.INGRESO, "descripcion": "Prueba", "monto": amount,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(Transaccion.objects.count(), 0)

    def test_reject_invalid_type(self):
        response = self.client.post(reverse("agregar_transaccion"), {
            "tipo": "transferencia", "descripcion": "Prueba", "monto": "10.00",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Transaccion.objects.count(), 0)

    def test_reject_blank_description(self):
        response = self.client.post(reverse("agregar_transaccion"), {
            "tipo": Transaccion.Tipo.INGRESO, "descripcion": "   ", "monto": "10.00",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Transaccion.objects.count(), 0)

    def test_list_shows_financial_totals(self):
        Transaccion.objects.create(tipo=Transaccion.Tipo.INGRESO, descripcion="Salario", monto=Decimal("100.00"))
        Transaccion.objects.create(tipo=Transaccion.Tipo.GASTO, descripcion="Comida", monto=Decimal("30.00"))
        response = self.client.get(reverse("lista_transacciones"))
        self.assertEqual(response.context["total_ingresos"], Decimal("100.00"))
        self.assertEqual(response.context["total_gastos"], Decimal("30.00"))
        self.assertEqual(response.context["balance"], Decimal("70.00"))
