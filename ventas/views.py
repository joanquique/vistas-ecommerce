from django.shortcuts import render, redirect
from django.http import HttpResponse

PRODUCTOS = [
    {"id": 1, "title": "Laptop Gamer", "price": 1500},
    {"id": 2, "title": "Mouse Pro", "price": 80},
    {"id": 3, "title": "Teclado RGB", "price": 120},
]

def ventas_home(request):
    carrito = request.session.get("carrito", [])
    return render(request, "ventas/ventas.html", {
        "productos": PRODUCTOS,
        "carrito": carrito,
    })

def agregar_carrito(request, product_id):
    carrito = request.session.get("carrito", [])
    carrito.append(product_id)
    request.session["carrito"] = carrito
    return redirect("ventas_home")

def procesar_pedido(request):
    request.session["carrito"] = []
    return HttpResponse("✅ Pedido procesado correctamente")
