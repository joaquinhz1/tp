from django import forms
from .models import Autor, Categoria, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class LibroSearchForm(forms.Form):
    titulo = forms.CharField(label="Buscar título", max_length=200)
