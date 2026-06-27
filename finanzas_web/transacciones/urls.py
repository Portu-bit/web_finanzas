from django.urls import path
from . import views

urlpatterns = [
    path('', views.transacciones_list, name='lista_transacciones'),
    path('agregar/', views.agregar_transaccion, name='agregar_transaccion')
]