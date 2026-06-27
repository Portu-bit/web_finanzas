from django.shortcuts import render, redirect
from .models import Transaccion
from .forms import TransaccionForm
# Create your views here.
def transacciones_list(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'transacciones/transacciones_list.html', {'transacciones': transacciones})

def agregar_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()
    return render(request, 'transacciones/agregar.html', {'form': form})