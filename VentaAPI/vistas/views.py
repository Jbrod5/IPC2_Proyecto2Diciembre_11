from django.shortcuts import render

def verInicio(request):
    return render(request, 'vistas/home.html')

def verClientes(request):
    return render(request, 'vistas/clientes.html')

def verFacturas(request):
    return render(request, 'vistas/facturas.html')

