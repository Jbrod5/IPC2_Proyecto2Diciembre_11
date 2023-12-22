# Modelo de Producto (controladores en models.py)
class Producto:
    def __init__(self, codigo, nombre, descripcion, precio, stock):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock

    def obtener_nombre_producto(self):
        return self._nombre
    def obtener_descripion(self):
        return self._descripcion
    def obtener_precio(self):
        return self._precio
    def obtener_stock(self):
        return self._stock
    def obtener_codigo(self):
        return self._codigo
    

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