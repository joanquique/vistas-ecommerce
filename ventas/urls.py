from django.urls import path
from .views import ventas_home, agregar_carrito, procesar_pedido, ventas_chart, SalesDataView, register

urlpatterns = [
    path("", ventas_home, name="ventas_home"),
    path("add/<int:product_id>/", agregar_carrito, name="agregar_carrito"),
    path("procesar/", procesar_pedido, name="procesar_pedido"),
    path("ventas-chart/", ventas_chart, name="ventas_chart"),
    path("api/ventas-data/", SalesDataView.as_view(), name="ventas_data"),
    path("register/", register, name="register"),
]
