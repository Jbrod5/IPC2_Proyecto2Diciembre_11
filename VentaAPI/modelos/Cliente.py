# Modelo de cliente (controladores en models.py)
class Cliente:
    def __init__(self, nit, nombre, direccion):
        self._nit = nit
        self._nombre = nombre
        self._direccion = direccion


    def establecer_nombre(self, nombre):
        self._nombre = nombre
    def establecer_nit(self, nit):
        self._nit = nit
    def establecer_direccion(self, direccion):
        self._direccion


    def obtener_nit(self):
        return self._nit
    def obtener_nombre_cliente(self):
        return self._nombre
    def obtener_direccion(self):
        return self._direccion