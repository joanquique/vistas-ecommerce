from django.urls import path
from .views import ventas_home, agregar_carrito, procesar_pedido

urlpatterns = [
    path("", ventas_home, name="ventas_home"),
    path("add/<int:product_id>/", agregar_carrito, name="agregar_carrito"),
    path("procesar/", procesar_pedido, name="procesar_pedido"),
]
