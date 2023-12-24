from django.urls import path
from . import views 

urlpatterns = [
    #path("", views.hello),
    #path("hola_html", views.hello_Html),

    #Ejemplo usando params:
    #path("hola_params-<str:nombre>", views.hello_con_params)
    path("obtener-todos-los-clientes", views.obtener_clientes),
    path("obtener-cliente:<str:nit>", views.obtener_cliente),
    path('ingresar-cliente', views.ingresar_cliente),
    path('eliminar-cliente', views.eliminar_cliente),
    path('actualizar-cliente', views.actualizar_cliente),

    path("obtener-todos-los-productos", views.obtener_productos),
    path("obtener-producto:<str:codigo>", views.obtener_producto),
    path('ingresar-producto', views.ingresar_producto),
    path('eliminar-producto', views.eliminar_producto),
    path('actualizar-producto', views.actualizar_producto),
]