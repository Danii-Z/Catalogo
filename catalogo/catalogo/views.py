from django.shortcuts import render
from productos.models import Producto

def inicio(request):
    template_name = "index.html"

    productos = Producto.objects.all()
    print(productos)
    contexto = {
        'productos': productos
    }
    return render(request, template_name, contexto)

