from django.contrib import admin
from .models import Usuario
from .models import Producto
# Register your models here.
admin.site.register(Usuario)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto', 'precioProducto', 'stockProd', 'imagen']
