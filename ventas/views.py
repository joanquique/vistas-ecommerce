from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

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

class SalesDataView(View):
    def get(self, request, *args, **kwargs):
        # Datos demo
        labels = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        values = [5, 8, 3, 10, 7, 12, 6]

        return JsonResponse({
            "labels": labels,
            "values": values
        })
        
def ventas_chart(request):
    return render(request, "ventas/ventas_chart.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login") 
    else:
        form = UserRegisterForm()

    return render(request, "ventas/register.html", {"form": form})