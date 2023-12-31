# Modelo de Producto (controladores en models.py)
class Producto:
    def __init__(self, codigo, nombre, descripcion, precio, stock):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock
        self._venta = 0

    def obtener_nombre(self):
        return self._nombre
    def obtener_descripion(self):
        return self._descripcion
    def obtener_precio(self):
        return self._precio
    def obtener_stock(self):
        return self._stock
    def obtener_codigo(self):
        return self._codigo
    def obtener_venta(self):
        return self._venta
    def obtener_diccionario(self):
        return self.__dict__

    def establecer_codigo(self, id):
        self._codigo = id
    def establecer_nombre(self, nombre):
        self._nombre = nombre
    def establecer_descripcion(self, descripcion):
        self._descripcion = descripcion
    def establecer_precio(self, precio):
        self._precio = precio
    def establecer_stock(self, stock):
        self._stock = stock
    def establecer_venta(self, venta):
        self._venta = venta