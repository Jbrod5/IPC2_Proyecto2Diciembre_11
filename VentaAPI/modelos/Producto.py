# Modelo de Producto (controladores en models.py)
class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock

    def obtener_nombre(self):
        return self._nombre
    def obtener_descripion(self):
        return self._descripcion
    def obtener_precio(self):
        return self._precio
    def obtener_stock(self):
        return self._stock
    def obtener_id(self):
        return self._id
    

    def establecer_id(self, id):
        self._id = id
    def establecer_nombre(self, nombre):
        self._nombre = nombre
    def establecer_descripcion(self, descripcion):
        self._descripcion = descripcion
    def establecer_precio(self, precio):
        self._precio = precio
    def establecer_stock(self, stock):
        self._stock = stock