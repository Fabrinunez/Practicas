from django.contrib import admin

# Register your models here.
admin.site.site_header = "Admon Cafetería Yuri"
admin.site.site_title = "Panel Cafetería Yuri"
admin.site.index_title = "Control de Operaciones"

from .models import Producto, Pedido

admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)

admin.site.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'estado', 'total', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente_nombre',)