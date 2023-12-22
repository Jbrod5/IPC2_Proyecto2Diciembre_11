from django.db import models

import json

from driver_xml.Cliente_BD import Cliente_BD
from driver_xml.Producto_BD import Producto_BD

from modelos.Cliente import Cliente
from modelos.Producto import Producto

# Create your models here.
# Django usa este archivo para crear modelos que a su vez son controladores, lo usaremos para hacer solo controladores
class Cliente_Controller:
    def __init__(self):
        self._cliente_bd = Cliente_BD()

    def ingresar_cliente_nuevo(self, cliente):
        """
        Ingresa un nuevo cliente haciendo las validaciones necesarias para ello
        """

        # Verificar que cliente sea una instancia de Cliente
        if isinstance(cliente, Cliente):

            # Verificar si el cliente contiene toda la informacion necesaria para ser almacenado
            valido = cliente.obtener_nombre() !=  None and cliente.obtener_nit() != None and cliente.obtener_direccion() != None
            
            if valido:
                self._cliente_bd.verificarClienteNuevo(cliente)
            
            else:
                print("El cliente que se intenta almacenar no contiene toda la informacion requerida")

        else:
            print("El cliente que se intenta agregar no es una instancia de cliente")
        


    def obtener_todos(self):
        """
        Retorna un string con el json de todos los clientes
        """
        lista_clientes = self._cliente_bd.obtenerTodosLosClientes()
        lista_diccionarios = []
        
        for i in range(len(lista_clientes)):
            diccionario = lista_clientes[i].obtener_diccionario()
            lista_diccionarios.append(diccionario) 

        json_string = json.dumps(lista_diccionarios)
        print(json_string)
        return json_string

    


class Producto_Controller:
    def __init__(self):
        self._producto_bd = Producto_BD()

    def ingresar_producto_nuevo(self, producto):
        """
        Ingresa un nuevo producto haciendo las validaciones necesarias para ello
        """

        # Verificar que cliente sea una instancia de Producto
        if isinstance(producto, Producto):

            # Verificar si el cliente contiene toda la informacion necesaria para ser almacenado
            valido = producto.obtener_nombre() !=  None and producto.obtener_descripion() != None and producto.obtener_precio() != None and producto.obtener_stock!= None and producto.obtener_codigo != None
            
            if valido:
                self._producto_bd.verificarProductoNuevo(producto)
            
            else:
                print("El producto que se intenta almacenar no contiene toda la informacion requerida")

        else:
            print("El producto que se intenta agregar no es una instancia de cliente")
        


    def obtener_todos(self):
        """
        Retorna un string con el json de todos los productos
        """
        lista_productos = self._producto_bd.obtenerTodosLosProductos()
        lista_diccionarios = []
        
        for i in range(len(lista_productos)):
            diccionario = lista_productos[i].obtener_diccionario()
            lista_diccionarios.append(diccionario) 

        json_string = json.dumps(lista_diccionarios)
        print(json_string)
        return json_string