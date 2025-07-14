# Proyecto Blog Django

Este proyecto es un blog simple en Django que incluye:

- Herencia de plantillas
- 3 modelos con sus formularios
- Búsqueda por título de Post
- Uso de Bootstrap
- Subido a GitHub

## Cómo probar

1. Clonar el repositorio y navegar al proyecto
2. Crear entorno virtual:
python -m venv env
source env/Scripts/activate (Windows)
source env/bin/activate (Linux/Mac)

markdown
Copiar
Editar
3. Instalar dependencias:
pip install -r requirements.txt

markdown
Copiar
Editar
4. Ejecutar migraciones:
python manage.py makemigrations
python manage.py migrate

markdown
Copiar
Editar
5. Correr el servidor:
python manage.py runserver

markdown
Copiar
Editar
6. Entrar a http://127.0.0.1:8000

## Funcionalidades

- Crear autores, categorías y posts desde `/nuevo_autor/`, `/nueva_categoria/`, `/nuevo_post/`
- Buscar posts desde `/buscar_post/`