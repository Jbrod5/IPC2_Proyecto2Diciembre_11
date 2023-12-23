from django.shortcuts import render

from django.http import HttpResponse,JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente_Controller
from .models import Producto_Controller

from modelos.Cliente import Cliente
from modelos.Producto import Producto

# Create your views here.

# CLIENTES ------------------------------------------------------------------------------------------------
def obtener_clientes(request):

    cliente = Cliente("123", "Pedro", "Dir 1")
    cliente2 = Cliente("456", "Maria", "Dir 2")

    controller = Cliente_Controller()

    controller.ingresar_cliente_nuevo(cliente)
    controller.ingresar_cliente_nuevo(cliente2)

    clientes = controller.obtener_todos()
    return JsonResponse(clientes, safe = False)


def obtener_cliente(request, nit):
    controller = Cliente_Controller()
    cliente_json = controller.obtener_cliente(nit)
    return JsonResponse(cliente_json, safe = False)

# POST
@csrf_exempt
def ingresar_cliente(request):
    if request.method == 'POST':

        controller = Cliente_Controller()

        nit = request.POST['nit']
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']

        cliente = Cliente(nit, nombre, direccion)
        controller.ingresar_cliente_nuevo(cliente)
        return HttpResponse("Cliente ingresado correctamente!")

# PRODUCTOS ----------------------------------------------------------------------------------------------

def obtener_productos(request):
    producto = Producto("1", "prod prueba", "este es un producto de prueba", 20, 30)
    producto2 = Producto("2", "prueba2", "este es el segundo prodcto de prueba", 4, 150)
    controller = Producto_Controller()

    controller.ingresar_producto_nuevo(producto)
    controller.ingresar_producto_nuevo(producto2)
    productos = controller.obtener_todos()
    return JsonResponse(productos, safe=False)

def obtener_producto(request, codigo):
    controller = Producto_Controller()
    producto_json = controller.obtener_producto(codigo)
    return JsonResponse(producto_json, safe = False)

# POST
@csrf_exempt
def ingresar_producto(request):
    if request.method == 'POST':

        controller = Producto_Controller()

        codigo = request.POST['codigo']        
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        producto = Producto(codigo, nombre, descripcion, precio, stock)
        controller.ingresar_producto_nuevo(producto)
        return HttpResponse("Producto ingresado correctamente!")
    
    