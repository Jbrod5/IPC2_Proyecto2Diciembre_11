from django.shortcuts import render

def verInicio(request):
    return render(request, 'vistas/home.html')

def verClientes(request):
    return render(request, 'vistas/clientes.html')

def verFacturas(request):
    return render(request, 'vistas/facturas.html')

def verProductos(request):
    return render(request, 'vistas/productos.html')

def verReportes(request):
    cantProd = 50
    return render(request, 'vistas/reporte.html', {
        'cantProd':cantProd
    })

