from django.db import models

import json

from driver_xml.Cliente_BD import Cliente_BD
from driver_xml.Producto_BD import Producto_BD
from driver_xml.Factura_BD import Factura_BD

from modelos.Cliente import Cliente
from modelos.Producto import Producto
from modelos.Factura import Factura
from modelos.ProductoGuia import ProductoGuia

from datetime import datetime

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
    
    def obtener_cliente(self, nit):
        """
        Retrorna un string con el json de un solo cliente en base al nit
        """

        cliente = self._cliente_bd.obtenerClienteEspecifico(nit)
        cliente_dic = cliente.obtener_diccionario()
        json_string = json.dumps(cliente_dic)
        return json_string
    
    def eliminar(self, nit):
        """
        Elimina un cliente en base a un nit, y returna True o False si se elimino correctamente
        """
        if nit != None:
            eliminado = self._cliente_bd.eliminarCliente(nit)
            return eliminado
        else: 
            print("El nit esta vacio")
            return False

    def actualizar(self, cliente):
        if cliente != None:

            if isinstance(cliente, Cliente):
                valido = cliente.obtener_nombre() !=  None and cliente.obtener_nit() != None and cliente.obtener_direccion() != None
            
                if valido:
                    nit = cliente.obtener_nit()
                    nombre = cliente.obtener_nombre()
                    direccion = cliente.obtener_direccion()
                    self._cliente_bd.actualizarCliente(nit, nombre, direccion)
            
            else: 
                print("El objeto no es una instancia de cliente")

        else: 
            print("No se paso una instancia")



class Producto_Controller:  # ----------------------------------------------------------------------------------------------------------
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

    def obtener_producto(self, codigo):
        """
        Retorna un string con el json del producto a buscar en base a su codigo
        """

        producto = self._producto_bd.obtenerProductoEspecifico(codigo)
        producto_dic = producto.obtener_diccionario()
        json_string = json.dumps(producto_dic)
        return json_string
    
    def eliminar_producto(self, codigo_producto):
        if codigo_producto == None:
            print('Producto no Encontrado')
            return False
        else:
            eliminado = self._producto_bd.eliminarProducto(codigo_producto)
            return eliminado
        
    def actualizar_producto(self, codigo_producto, nombre, descripcion, precio, stock):
        
        valido = codigo_producto != None and nombre != None and descripcion != None and precio != None and stock != None
        
        if valido:
            actualizar = self._producto_bd.actualizarProducto(codigo_producto, nombre, descripcion, precio, stock)
            return actualizar
        else:
            print('Fallo al actualizar el producto')
            return False
        


class Factura_Controller:  # ------------------------------------------------------------------------------------------------------

    def __init__(self):
        self._factura_bd = Factura_BD()

    def ingresar_factura_nueva(self, factura, lista_codigos, lista_cantidades):
        """
        Ingresa una factura nueva a la base de datos haciendo las validaciones necesarias
        """
        if isinstance(factura, Factura):
            valido = factura.obtener_nit() != None 

            # Se guarda la fecha actual en la factura
            fecha_actual = datetime.now()
            fecha_actual_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
            factura.establecer_fecha_emision(fecha_actual_str)
            
            # Recorrer las listas de productos y cantidades para agregarlos a la factura
            contador = 0
            while contador < len(lista_cantidades):
                codigo = lista_codigos[contador]
                cantidad = lista_cantidades[contador]
                
                # Actualizar la cantidad de ventas del prodcto y su stock
                producto_bd = Producto_BD()
                producto_bd.actualizarStockYVentas(codigo, cantidad)
                
                # Asignar producto guia a la factura
                producto = ProductoGuia(codigo, cantidad)
                factura.agregarProducto(producto)
                print(producto.obtener_diccionario_producto_guia())
                contador +=1

            self._factura_bd.ingresarFactura(factura)


    def obtener_todas (self):
        """
        Retorna un string con el json de todas las facturas
        """

        lista_facturas = self._factura_bd.obtenerTodasLasFacturas()
        lista_diccionarios = []

        for i in range ( len (lista_facturas) ):
            diccionario = lista_facturas[i].obtener_diccionario()
            lista_diccionarios.append(diccionario)

        json_string = json.dumps(lista_diccionarios)
        print(json_string)
        return json_string
    
    def obtener_facturas_cliente(self, nit):
        """
        Retorna todas las facturas de un cliente en especifico
        """

        lista_facturas = self._factura_bd.obtenerFacturasDeUnClienteEspecifico(nit)
        lista_diccionarios = []

        for i in range ( len (lista_facturas) ):
            diccionario = lista_facturas[i].obtener_diccionario()
            lista_diccionarios.append(diccionario)

        json_string = json.dumps(lista_diccionarios)
        #print(json_string)
        return json_string

    def eliminar_factura(self, numero_factura):
        """
        Elimina una factura en base a su numero correlativos
        """

        if numero_factura != None:
            self._factura_bd.eliminarFactura(numero_factura)
             
        else: 
            print("No hay un numero valido de factura para eliminar")