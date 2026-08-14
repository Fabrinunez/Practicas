#EL serializador de pedidos es el encargado de convertir los datos del modelo "pedido" a su formato json
from rest_framework import serializers
from pedidos.models import Producto, Pedido

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        