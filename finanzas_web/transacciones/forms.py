from django import forms
from .models import Transaccion


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ["tipo", "descripcion", "monto"]
        widgets = {
            "descripcion": forms.TextInput(attrs={"maxlength": 255}),
            "monto": forms.NumberInput(attrs={"min": "0.01", "step": "0.01"}),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"].strip()
        if not descripcion:
            raise forms.ValidationError("La descripción no puede estar vacía.")
        return descripcion
