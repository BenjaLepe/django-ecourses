# 🎓 Ecourses

Aplicación web desarrollada con Django, en la cualpodrás administrar tu rendimiento académico.

## 🔨 Project setup

Primero debemos configurar el entorno virtual:
```powershell
# Creamos el entorno virtual
python -m virtualenv venv
# Activamos el entorno
./venv/Scripts/activate
# Instalamos las dependencias
pip install -r requirements.txt
```

Una vez instaladas las dependencias, se deben correr las migraciones:

```powershell
python manage.py migrate
```

Finalmente, levantamos el servidor:
```powershell
python manage.py runserver
```

Por defecto, se encuentra el siguiente usuario:
```json
{
    username: "testuser",
    password: "prueba123"
}
````
