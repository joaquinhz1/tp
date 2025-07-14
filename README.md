# Blog en Django

Este es un proyecto simple de blog en Django para la consigna:

## Funcionalidades:

- Herencia de plantillas (base.html, etc.)
- Modelos: Autor, Categoría, Entrada
- Formularios para insertar datos en cada modelo
- Formulario de búsqueda por título de entrada

## Cómo usar:

1. Crear entorno virtual:

```bash
python -m venv env
source env/bin/activate  # en Linux/macOS
env\Scripts\activate   # en Windows
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Levantar el servidor:

```bash
python manage.py runserver
```

5. Acceder desde: http://127.0.0.1:8000/

