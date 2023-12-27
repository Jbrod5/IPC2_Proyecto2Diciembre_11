from django.shortcuts import render

def verInicio(request):
    return render(request, 'vistas/home.html')

def verClientes():
    return render()

