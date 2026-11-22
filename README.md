# Finanzas Web

Aplicación web de control financiero personal construida con Django y SQLite. Permite registrar ingresos y gastos y consultar un resumen del balance.

## Funcionalidades
- Listado y registro de transacciones.
- Validación de tipo, descripción y monto positivo.
- Resumen de ingresos, gastos y balance.
- Protección CSRF y configuración sensible mediante variables de entorno.
- Pruebas automatizadas y GitHub Actions.

## Requisitos
Python 3.11 y pip.

## Instalación local (Windows PowerShell)
Desde la raíz del repositorio:

```powershell
cd finanzas_web
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Genera una clave con `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` y reemplaza el valor de SECRET_KEY en .env.

## Migraciones y ejecución
```powershell
python manage.py migrate
python manage.py runserver
```
Abre http://127.0.0.1:8000/transacciones/.

## Pruebas
```powershell
python manage.py test
```

## Despliegue
El Procfile utiliza Gunicorn. Configura SECRET_KEY, DEBUG=False, ALLOWED_HOSTS con los dominios reales y CSRF_TRUSTED_ORIGINS con los orígenes HTTPS. No uses la clave de ejemplo ni ALLOWED_HOSTS=*.

Configura almacenamiento persistente para SQLite o una base de datos gestionada: algunos proveedores eliminan los archivos locales al reiniciar o desplegar.

## Base de datos
Se conserva la base de datos que ya estaba versionada para no eliminar datos sin autorización. No publiques bases con información personal. El .gitignore impide añadir nuevas bases locales.
