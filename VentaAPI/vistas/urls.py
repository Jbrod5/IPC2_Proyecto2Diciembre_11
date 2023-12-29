from django.urls import path
from . import views 

urlpatterns = [
    #path("", views.hello),
    #path("hola_html", views.hello_Html),
    path('inicio/', views.verInicio),
    path('facturas/', views.verFacturas),
    path('clientes/', views.verClientes),
    path('productos/', views.verProductos),
    path('reportes/', views.verReportes),
]