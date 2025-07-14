# Proyecto Django: Biblioteca

## 🚀 Instalación rápida
1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
2. Instalar dependencias:
```bash
pip install django
```
3. Migrar DB:
```bash
python manage.py migrate
```
4. Ejecutar servidor:
```bash
python manage.py runserver
```

## ✅ Funcionalidades
- Crear autores, categorías y libros.
- Buscar libros por título.
- Ver listado de libros.

## 📂 Estructura
- `gestion/models.py`: modelos
- `gestion/forms.py`: formularios
- `gestion/views.py`: vistas
- `gestion/templates`: templates con herencia
