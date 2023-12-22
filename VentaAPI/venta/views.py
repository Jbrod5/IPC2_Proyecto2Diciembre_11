from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Cliente_Controller
from .models import Producto_Controller

from modelos.Cliente import Cliente
from modelos.Producto import Producto

# Create your views here.
def obtener_clientes(request):

    cliente = Cliente("123", "Pedro", "Dir 1")
    cliente2 = Cliente("456", "Maria", "Dir 2")

    controller = Cliente_Controller()

    controller.ingresar_cliente_nuevo(cliente)
    controller.ingresar_cliente_nuevo(cliente2)

    clientes = controller.obtener_todos()
    return JsonResponse(clientes, safe = False)

def obtener_productos(request):
    producto = Producto("1", "prod prueba", "este es un producto de prueba", 20, 30)
    producto2 = Producto("2", "prueba2", "este es el segundo prodcto de prueba", 4, 150)
    controller = Producto_Controller()

    controller.ingresar_producto_nuevo(producto)
    controller.ingresar_producto_nuevo(producto2)
    productos = controller.obtener_todos()
    return JsonResponse(productos, safe=False)