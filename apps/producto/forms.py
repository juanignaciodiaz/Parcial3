
from django.forms import fields, widgets
from apps.producto.models import Categoria, Producto
from django import forms


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        widgets = {
            'nombre': forms.TextInput(attrs={'name':'titulo_producto', 'id':'titulo_producto', 'placeholder': 'Titulo del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'crear-producto-precio', 'name':'precio_producto', 'id':'precio-producto', 'placeholder': 'Precio del producto'}),
            'stock': forms.NumberInput(attrs={'class': 'crear-producto-stock', 'placeholder': 'Stock del producto'}),
            'categoria': forms.Select(attrs={'class': 'lista-categoria'}),
            # 'imagen': forms.FileInput(attrs={'id': 'campo-imagen'}),
        }
        fields = ('nombre', 'precio', 'stock', 'categoria', 'estadooferta', 'imagen')