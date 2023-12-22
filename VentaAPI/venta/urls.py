from django.urls import path
from . import views 

urlpatterns = [
    #path("", views.hello),
    #path("hola_html", views.hello_Html),

    #Ejemplo usando params:
    #path("hola_params-<str:nombre>", views.hello_con_params)
    path("obtener-todos-los-clientes", views.obtener_clientes),
    path("obtener-todos-los-productos", views.obtener_productos),
]